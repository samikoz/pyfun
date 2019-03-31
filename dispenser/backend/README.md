# Dispenser
A simulation of a cash dispenser written as a two-day recruitment task

## Usage
To launch the dispenser run `dispenser.py [amount]`, where `[amount]` 
is the amount of money to withdraw, with a Python interpreter of 
version >= 3.6

## Todo
1. Draw architecture diagram
2. Describe the diagram, describe the classes
3. Rethink dispenser_types: rename the file, introduce note type,
allow for infinity in number of notes, ProcessorChain inheriting from
Navigator
4. Introduce a chain of handlers similar to processors - or get rid
of handlers and put this logic into the request itself. Then won't
have to have two separate request abstract classes
5. Rethink the logic of mutual acknowledging between navigator and
processor chains (and handlers)
6. Rethink how much logic to pass to abstract Dispenser. Navigator will
have to be exposed to allow for init extension
7. For each class rethink which fields deserve getters to allow
extension as above
8. Inspect tests and mocks; do not test internals (e.g. processor)
9. Inspect RegularNoteProcessor's logic
