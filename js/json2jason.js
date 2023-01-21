;(() => {
"use strict"

const toJason = (k, v, omitKey) => {
	k = escapeHtml(JSON.stringify(k)) + ": "
	if (omitKey)
		k = ""
	if (typeof v === "object" && v && Object.entries(v).length) {
		const isArr = Array.isArray(v)
		const lbrace = isArr ? "[" : "{"
		const rbrace = isArr ? "]" : "}"
		const listTag = isArr ? "ol" : "ul"
		return `<details open="open">` +
			`<summary>${k}${lbrace}</summary>` +
			`<${listTag}>` +
			`<li>` +
			Object.entries(v)
				.map(([k, v]) => toJason(k, v, isArr))
				.join(`,</li><li>`) +
			`</li>` +
			`</${listTag}>` +
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
})();
