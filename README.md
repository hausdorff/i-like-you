# i like you

[hetexted.com](http://www.hetexted.com) is a website where confused twentysomethings send in text messages they've received from boys, and the users of the website vote on whether the boy likes them.

To me this was begging to be turned into a machine learning classifier.

In this project, I:

1. scraped all of the lazy-loading front page using the JavaScript commands in `get-data.js`
2. lifted all the images out of the resulting HTML using `get_data.py`
3. lifted text out of images using `proc_images.py`
4. and trained a bag of words classifier.

The pipeline is fragile. I'm putting it online basically to document it.

# Dependencies

* `tesseract`, `pytesser`, and `opencv` are required for `get_data.py`

#LICENSE

Distributed under MIT license, basically meaning you can do what you want, but you have to note in the source that your stuff is adapted from my stuff. Though let's face it, using this code for anything except judging how bad of a coder I am is probably a really bad idea.