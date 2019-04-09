# Dispenser
A simulation of a cash dispenser written for a recruitment process and
later enhanced to serve as a code sample.

## Assumptions

## Usage

## Todo
1. ChainDivisor spits out a Request object which can be queried for a note
and returns how many to dispense. Request has to expose method checking 
whether the amount is exhausted. Then something has to supervise the
individual dispensing. Think whether ChainDivisor operates on Request
internally (atm it does). Test it, correct typing.
2. Make sure internals of no object are compromised. Rethink
where getters and setters are appropriate.
3. Rethink dispenser_types: rename the file, introduce note type,
allow for infinity in number of notes
4. Inspect tests and mocks; do not test internals (e.g. processor)
5. Inspect RegularNoteProcessor's logic
6. Think about dispense's return type