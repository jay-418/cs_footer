# cs_footer

## Purpose
Hold resources, tools, and html for creating well formatted message templates in JitBit.
> Note: Because JitBit strips all class, alt, and id, and all elements other than div from messages nestling multiple divs allows targeted icon formatting within pre-formatted messages that can't use class or id

## Contents
- [Original html](./footer.html)
- [Minification script](./minify.py)
- [Folder with icons](./icons)

## To Use
Make changes first to `footer.html`, then run `minify.py` to remove line breaks. Then copy the contents of `footer-min.html` into JitBit message template.
