Add `api.twisted_publish()`, a function to publish messages from within a consumer callback (remember to use `twisted.internet.threads.blockingCallFromThread()` when calling it, or `reactor.callFromThread()`)