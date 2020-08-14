# action-example
This action prints "Hello action" or "Hello"+ the name of person to greet to the log

## Inputs
### `who-to-greet`
**Required** The name of the person to greet. Default "action"

## Outputs
### `time`
The time person was greeted

|tablecol|col2|col3|
|--------|----|-----|


[comment]: <> (This is a comment, it will not be included)
## Example usage
uses: actions-example
with:
  who-to-greet: 'Mona the Octocat'
