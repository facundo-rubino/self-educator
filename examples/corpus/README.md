# examples/corpus

Sample documents for the `files` source, so `edu run` and the test suite work
with no network and no API key. Delete these and point `sources.files.paths` at
your own directory — or drop `files` from `sources.order` entirely once you
have real sources configured.

`.md` files use their H1 as the title. `.json` files may carry a `metrics`
object; that is how a local corpus exercises the engagement-based scorers.
