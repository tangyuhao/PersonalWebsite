When I was developing my website, I faced an annoying problem:
I have an fixed header on the top of my web pages thus if I would like to use html anchors directly, my header will cover the anchored place.
**Note:** [What is anchor in html?](https://www.w3.org/TR/html4/struct/links.html)

After searching for resolutions on the Internet, I found a solution which is really easy to implement.

## How to set anchors for specified elements
I only want give `<h2>` and `<h3>` anchors, their id all have the form of `toc_<num>` thus I first use 

```js
var titles = $("h2[id^='toc_'],h3[id^='toc_']")
```
to get all qualified h2 and h3 nodes.
Then for each of them, I can create a link to them by using:

```html
<a href="#toc_<num>">link</a> <!--num should replaced with corresponding number-->
```
But this causes the problem I just mentioned. We need some tricks to "offset" the position of anchors.

## Create new offset anchors
We need to create new anchors for each headline node:

```js
for (title of titles){
    tagid = title.id + "tag";
    var new_tag = $("<span></span>",{"id":tagid});
    // don't use title directly!!!!
    // if you use title.append(new_tag) then you will get [object object] after the node you want to append
    $("#"+title.id).append(new_tag);
    }
```

The above code can create a new `<span>` tag inside each `h2` or `h3`:

```html
<h2 id="toc_4">title<span id="toc_4tag"><span></h2>
```
Then just for each of them, create links:

```html
<a href="#toc_<num>tag">link</a> 
```
Then you are all set!
Wait! Nothing changes? Oh, you need to add some `css` styles for your new anchors!

## Add new css styles for anchors
Last step is to change the style of `<span>` to let it has a relative position of `-80px`, which looks best for my page header.

```css
h3{ position:relative; }
h2{ position:relative; }
h2 span{ position:absolute; top:-80px;}
h3 span{ position:absolute; top:-80px;}
```
Then when you click the links to anchors, the position of your headlines will offset by 80px downward!


