---
title: "Online Article Tools"
author: "Main navigation"
date: ""
category: "anarchism"
source: "https://libcom.org/article/online-article-tools"
source_name: "libcom.org"
page_type: book
mirror_state: none
language: "en"
description: "Links to helpful online tools for assisting with putting together articles and content for libcom.org."
tags:
  - "en"
  - "anarchism"
  - "libcom"
files:
  []
---

[Read on libcom.org](https://libcom.org/article/online-article-tools)

Links to helpful online tools for assisting with putting together articles and content for libcom.org.

Wojtek, thought you might like the merge PDF one! If you fancied merging some of the PDFs of your library submissions that would be really cool, if you had time…

On a related note, does anyone know a good online OCR tool? That would be something we could add in here

Reminder to myself to add these: http://www.howtogeek.com/166610/who-needs-a-scanner-scan-a-document-to-pdf-with-your-android-phone/ and https://play.google.com/store/apps/details?id=com.intsig.camscanner&hl=en_GB

The LibeOffice suite is pretty good and all of its programs can export files as pdfs.

cutepdf I get an out of date Java warning, not sure if it still works.

Google Docs does OCR now. (I know... flipping Google, but it works.)

Speechmatics is commercial software with a pretty decent free plan. AI-assisted speech-to-text, translation, subtitling etc. Good for making transcripts of audio interviews, though they still need proofing.

- Gimp is also a handy (open-source) image-manipulation tool for modifying article images (resizing etc.) - For general OCR you can also use the (open-source) program gImageReader ; besides OCRing PDFs, it also allows you to open a screenshot or image of text and then extract the text from it ( here's a video )

This is good for cropping PDFs - https://www.sejda.com/crop-pdf

This is a good alternative to some of the tools already listed - https://www.ilovepdf.com/

"FWO Formatter: A tool for getting rid of excess of line breaks in your text."

Fozzie wrote: "FWO Formatter: A tool for getting rid of excess of line breaks in your text."

If anyone would like to save PDFs from archive.org that are only set up to be borrowed, there is a tool for that now:

https://github.com/elementdavv/internet_archive_downloader?tab=readme-ov-file

Nice one. I've always just used a cache-reading program. You can basically borrow whatever book on the IA and then flip through all the pages. As you flip through it, your browser stores cached images of each page, which you can then use a cache-reading program to save. You can also just view/save the files directly from the cache-folder of your browser, without using any other program. Then all you have to do is combine the individual page-images into a pdf file. But yeah, I'm sure there are some automated tools out there that are much easier to use!

If you're on Linux, there are quite a few command-line programs that you can use to work with PDFs (they might also work on Winblows, but I haven't checked). They're much quicker if you're working with large amounts of data, especially when used together in a script...

"magick" can be used to combine image files together into a single pdf (and perform other operations on images).

"mat2" can be used to remove whatever metadata, but it seems to remove the ocr text layer too, so I haven't really been using it.

You can then combine all the above tools into a script. Something like this if you want to combine all the images in a directory into a pdf and then ocr it:

# combine jpg images into pdf; a quality of 70 should be fine

As far as online stuff, pdf24 also has a ton of tools, which are all free to use without any daily limits.
