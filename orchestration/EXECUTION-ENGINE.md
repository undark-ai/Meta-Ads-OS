# Execution engine

How the execution lane is driven. The contract is `EXECUTION-PROTOCOL.md`; this is the mechanism.

## Separate runs, always

An execution run has its own run id and its own directory. It never shares either with an audit.

```
audits/<run-id>/     an audit. Read-only. Describes the account.
changes/<run-id>/    an execution run. Mutates the account.
```

The separation is what lets a reader trust that the account an audit describes is the account it
measured. An audit that fixed things it found would be describing a state that no longer exists
by the time anyone reads it.

## Lifecycle

```
initialized → planning → awaiting_approval → previewing → applying → awaiting_activation
                                ↓                              ↓              ↓
                            rejected                        failed        completed
```

`awaiting_approval` and `awaiting_activation` are **blocking** states. There is no timeout that
resolves them, and no inference that resolves them either — silence is not consent, and an
approval given for an earlier change is not an approval for this one.

## Tool gating

Every call is checked against `schemas/meta-mcp-tool-classification.yaml` before it is made:

| Classification | Audit lane | Execution lane |
|---|---|---|
| `read` | allowed | allowed |
| `write` | **refused** | allowed, after approval |
| unclassified | **refused** | **refused** |

Unclassified fails closed in both lanes. If Meta ships a tool this repository has not seen,
nothing calls it until a human has classified it.

## Create-paused

The create chain always sets `PAUSED`. Activation is a distinct step that re-enters
`awaiting_approval`.

Between the two, the engine runs the pre-activation check: budget against **account history**
rather than against the plan, previews looked at, destination URLs resolved through their
redirect chains, exclusions present, optimisation event matching the objective.

This ordering is the point. A paused mistake costs nothing; a live one starts spending at
whatever budget the mistake specified.

## Logging

`applied.md` is written **as each call returns**, never batched. Per call: timestamp, tool,
entity id and name, before value, after value, and the plan line it implements.

Failures are logged with their error. A run that dies halfway must leave a complete record of
what it already did — a half-applied change set nobody wrote down is indistinguishable from
sabotage when someone opens the account tomorrow.

## Rollback

`rollback.md` is generated **during** the run from the captured before-values, not reconstructed
afterwards.

What rollback cannot restore, and what the plan must therefore say before the change is made:
learning phase (reversing an edit does not un-reset it), delivery history, spend already
incurred, event-configuration history, and audience membership history.

## Refusal is a normal outcome

The engine stops and reports rather than proceeding when the change exceeds its approval, the
finding behind it is unreconciled or below the volume floor, the measurement verdict is `RED`, a
customer-data upload is missing authorisation or hashing, or the account id does not match the
plan.

A refused run that explains itself is a successful run.
