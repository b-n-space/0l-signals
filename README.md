# 0L-Signals

Signaling tool for [0L Network](https://0l.network/) participants.

Available at https://signals.openlibra.space

## Todos

- [ ] Fetch proposals from a GitRepository. This is used in `get_proposals`

  Say `https://github.com/0LNetworkCommunity/libra/tree/main/ol/documentation/proposals` or wherever we decide to host
  proposals

- [ ] Fetch proposal stats from RPC and calculate counts and weights for its options.

  I believe this has to be a full archive or from the explorer

- [ ] Improve proposal page; display description, options, and addresses.
  Make the addresses clickable to copy; both address and ol command

- [ ] Utilise cache when calculating proposal stats

- [x] Deploy somewhere

> 1K GAS bounty for each task from `nourspace#6652`

## Docker

```shell
# Build
docker build -t 0l-signals .  

# Run
docker run -p 8000:8000 --rm 0l-signals
```
## Resources

- https://www.chartjs.org/
- https://vuejs.org/
- https://bulma.io/
- https://www.fontsquirrel.com/fonts/jockey-one
