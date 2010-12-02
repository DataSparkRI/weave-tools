==================================
 Weave Client-Side JavaScript API
==================================

Getting started
===============

The following two JavaScript files are required and need to be loaded in your HTML document, typically inside the ``<head>`` tag:

::

	<script type="text/javascript" src="path/to/lib/swfobject/swfobject/swfobject.js"></script>
	<script type="text/javascript" src="path/to/weave.js"></script>

The API will look for the ID ``Weave`` in the DOM to embed the Weave Flash object. Add the ID ``Weave`` to the element where Weave should be embedded:

::

	<div id="Weave">
		<p>Weave Container</p>
	</div>

If Weave cannot be loaded, the alternative content inside that tag will show on your web page.


Start using the API
===================

The function ``Weaveready()`` is called when the API becomes available in the Weave Flash object.

Example:

::

	<script language="JavaScript" type="text/javascript">
		function Weaveready(Weave) {
			alert(Weave.getSessionState([]));
		}
	</script>