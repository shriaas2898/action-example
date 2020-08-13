# action-example
This action prints "Hello action" or "Hello"+ the name of person to greet to the log

## Inputs
### `who-to-greet`
**Required** The name of the person to greet. Default "action"

## Outputs
### `time`
The time person was greeted

## Example usage
uses: actions/hello-world-javascript-action@v1
with:
  who-to-greet: 'Mona the Octocat'
