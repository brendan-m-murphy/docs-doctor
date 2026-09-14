Customising the model
=====================

Use this guide when the built-in workflows do not express the science you need. It
shows how to replace a likelihood or supply a custom model component.

Change the likelihood
---------------------

Implement a likelihood function when the supported likelihoods do not fit the required
error model.

Sampled tau is a separate extension; the production cached sampler is the matched
recipe below.

Run the production cached-amplitude recipe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``run_fixed_ou_cached`` is the first-class production route for the fixed-tau model.
It pairs the site-amplitude and state steps and reuses cached state updates. The
standard implementation remains the fallback.

The runner supports fixed positive timescales and independently inferred site
amplitudes.
