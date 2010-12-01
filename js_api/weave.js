function weaveAPIcheck () {
	try {
		var Weave = document.getElementById('Weave');
		var weaveSessionState = Weave.getSessionState([]);
		// API loaded, now what?
		Weaveready(Weave);
		return true;
	}
	catch (err) {
		// not yet loaded, check again
		setTimeout('weaveAPIcheck()', 1000);
		return false;
	}
}

/* 
	swfobject.embedSWF(
	swfUrl, 
	id, 
	width, height, 
	version, 
	expressInstallSwfurl, 
	flashvars, params, attributes, 
	callbackFn)
*/

swfobject.embedSWF(
	'/weave.swf', 
	'Weave', 
	'780', '420', 
	'9.0.0',
	'lib/swfobject/swfobject/expressInstall.swf',
	{},{},{},
	function(e) {
		if(e.success) {
			// Weave successfully embedded, now checking for API
			// in dumb 1sec intervalls
			setTimeout('weaveAPIcheck()', 1000);
		};
	}
);