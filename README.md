# action-example
This action prints "Hello action" or "Hello"+ the name of person to greet to the log

## Inputs
### `who-to-greet`
**Required** The name of the person to greet. Default "action"

## Outputs
### `time`
The time person was greeted

## Example usage
uses: actions-example
with:
  who-to-greet: 'Mona the Octocat'
