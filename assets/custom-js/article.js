$(document).ready(function() {
    article_createNav();
});
function article_createNav(){
    var titles = $("h2[id^='toc_'],h3[id^='toc_']");
    var TitleH2 = $("");
    var article_nav_node = $("<ul class=\"list-group list-group-bordered list-group-noicon uppercase\"></ul>");
    var ulNode = $("<ul></ul>");
    var lastTitleName = "H2";
    for (title of titles){
        //console.log(title.nodeName)
        if (title.nodeName === "H2"){

            // old title
            if (lastTitleName === "H3"){
                TitleH2.append(ulNode);
                //console.log(TitleH2.children())
                var tempNode = TitleH2.children();
                tempNode[0].classList.add("dropdown-toggle");
            }
            article_nav_node.append(TitleH2);

            // new title
            TitleH2 = article_createTitleH2(title);
            ulNode = $("<ul></ul>");
            lastTitleName = "H2";
        }
        else if (title.nodeName === "H3"){
            ulNode.append(article_createTitleH3(title));
            lastTitleName = "H3";
        }
    }
    $("#article_nav").append(article_nav_node);
}

function article_createTitleH2(node){
    var topNode = $("<li class=\"list-group-item\"></li>");
    var name = $("<a  href=\"#"+node.id+"\">"+node.innerHTML+"</a>");
    topNode.append(name);
    return topNode;
}

function article_createTitleH3(node){
    var retNode = $("<li><a href=\"#"+node.id+"\">"+node.innerHTML+"</a></li>")
    return retNode;
}
