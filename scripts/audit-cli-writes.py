#!/usr/bin/env python3
"""Enumerate the mutating subcommands exposed by tools/clis/*.js.

Method (stated so the result is reproducible, not hand-curated):
  1. Parse each CLI's nested `case '<name>':` labels into "<group> <subcommand>" pairs.
  2. Flag a pair as MUTATING when the subcommand name matches a state-changing verb
     (create/update/delete/pause/enable/... ) OR its body issues a `:mutate` call.
  3. Read-style POSTs (query/report/search endpoints) are therefore not flagged
     just for being POSTs — the subcommand name decides.

Prints a markdown table; --check compares against tools/clis/README.md and exits
non-zero if the two disagree.
"""
import io, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

MUTATING = re.compile(r'^(create|update|delete|remove|pause|enable|disable|add|set|send|'
                      r'upload|import|archive|subscribe|unsubscribe|tag|untag|publish|'
                      r'schedule|start|stop|cancel|revoke|assign|move|merge|push|post|'
                      r'invite|reset|apply|activate|deactivate|bulk)$')

def commands(path):
    """Yield (group, sub, body) triples from nested case labels."""
    src = io.open(path, encoding='utf-8').read()
    # indentation tells us group (shallower) from subcommand (deeper)
    labels = [(m.start(), len(m.group(1)), m.group(2))
              for m in re.finditer(r"\n([ \t]*)case '([^']+)':", src)]
    out, group, gindent = [], None, None
    for i, (pos, indent, name) in enumerate(labels):
        end = labels[i + 1][0] if i + 1 < len(labels) else len(src)
        if gindent is None or indent <= gindent:
            group, gindent = name, indent
            continue
        out.append((group, name, src[pos:end]))
    return out

rows = []
for path in sorted(glob.glob('tools/clis/*.js')):
    tool = os.path.basename(path)[:-3]
    muts = []
    for group, sub, body in commands(path):
        if MUTATING.match(sub) or ':mutate' in body:
            muts.append('%s %s' % (group, sub))
    if muts:
        rows.append((tool, sorted(set(muts))))

table = ['| CLI | Mutating subcommands (never invoke during an audit) |',
         '|---|---|']
for tool, muts in rows:
    table.append('| `%s` | %s |' % (tool, ', '.join('`%s`' % m for m in muts)))
md = '\n'.join(table)

if '--check' in sys.argv:
    readme = io.open('tools/clis/README.md', encoding='utf-8').read()
    missing = [t for t, _ in rows if '`%s`' % t not in readme]
    if missing:
        print('FAIL: tools/clis/README.md does not list: %s' % ', '.join(missing))
        sys.exit(1)
    print('OK: all %d CLIs with mutating subcommands are listed in tools/clis/README.md' % len(rows))
else:
    print(md)
    print('\n%d of %d CLIs expose at least one mutating subcommand.'
          % (len(rows), len(glob.glob('tools/clis/*.js'))))
