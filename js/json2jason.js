;(() => {
"use strict"

const toJason = (k, v, omitKey) => {
	k = escapeHtml(JSON.stringify(k)) + ": "
	if (omitKey)
		k = ""
	if (v && typeof v === "object" && Object.entries(v).length) {
		const isArr = Array.isArray(v)
		const lbrace = isArr ? "[" : "{"
		const rbrace = isArr ? "]" : "}"
		if (isArr)
			v = arr2html(v)
		else
			v = obj2html(v)
		return `<details open="open">` +
			`<summary>${k}${lbrace}</summary>` +
			v +
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
		return toJason(k, v, false)
	}).join(`,</li><li>`) + `</li></ul>`
}

const arr2html = (v) => {
	return `<ol><li>` + v.map(v => {
		return toJason("", v, true)
	}).join(`,</li><li>`) + `</li></ol>`
}
})();
