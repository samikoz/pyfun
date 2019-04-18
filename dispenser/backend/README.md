# Dispenser
A simulation of a cash dispenser written for a recruitment process and
later enhanced to serve as a code sample.

## Assumptions

## Usage

## Todo
0. Make the application work
1. ChainDivisor into DivisionFactory initiated with ContainerChain
with single method divide(amount) producing Division(amount) object 
to be accepted by ContainerChain. All dividing logic moved to Division
2. Make sure internals of no object are compromised. Rethink
where getters and setters are appropriate.
3. Rethink dispenser_types: rename the file, introduce note type,
allow for infinity in number of notes
4. Inspect tests and mocks; do not test internals (e.g. processor)
5. Think about dispense's return type
6. Order dispenser_types bottom-up and mark it with a comment