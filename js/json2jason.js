;(() => {
"use strict"

const type = (v) => Object.getPrototypeOf(v).constructor.name

const json2htmldoc = (d) => {
	return `<!DOCTYPE html>
<html lang="en">
<head>
	<title>jason - JSON viewer</title>
	<meta charset="utf-8" />
	<link rel="stylesheet" href="css/main.css" />
</head>
<body>
	<section id="json-viewer">` + json2html("", d, true) + `</section>
</body>
</html>`
}

const json2html = (k, v, omitKey) => {
	k = escapeHtml(JSON.stringify(k)) + ": "
	if (omitKey)
		k = ""
	if (v && type(v) in TYPES && Object.keys(v).length) {
		const [lbrace, rbrace, v2html] = TYPES[type(v)]
		return `<details open="open">` +
			`<summary>${k}${lbrace}</summary>` +
			v2html(v) +
			`</details>${rbrace}`
	}
	return k + escapeHtml(JSON.stringify(v))
}

const escapeHtml = (s) => {
	return s
		.replaceAll("&", "&amp;")
		.replaceAll("<", "&lt;")
		.replaceAll(">", "&gt;")
}

const obj2html = (v) => {
	return `<ul><li>` + Object.entries(v).map(([k, v]) => {
		return json2html(k, v, false)
	}).join(`,</li><li>`) + `</li></ul>`
}

const arr2html = (v) => {
	return `<ol><li>` + v.map(v => {
		return json2html("", v, true)
	}).join(`,</li><li>`) + `</li></ol>`
}

const TYPES = {
	Object: [`{`, `}`, obj2html],
	Array:  [`[`, `]`, arr2html],
}

})();
