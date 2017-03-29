$(document).ready(function() {
    article_createNav();

    setTimeout(reading_num_add,20000);// reading after 20s will increase the counter
    $("#comment_form").submit(article_comment_submit);
});
function article_createNav(){
    var titles = $("h2[id^='toc_'],h3[id^='toc_']");
    if (titles.length < 2){
        $("#right_div").remove();
        // if there is no titles, then let article fill all colomns
        $("#left_div").removeClass("col-md-9 col-sm-9").addClass("col-md-12 col-sm-12")
        // $("#article_nav").css("display","none")

        return;
    }
    


    var TitleH2 = $("");
    var article_nav_node = $("<ul class=\"list-group list-group-bordered list-group-noicon uppercase\"></ul>");
    var ulNode = $("<ul></ul>");
    var lastTitleName = "H2";
    for (title of titles){
        //console.log(title.nodeName)
        if (title.nodeName === "H2"){

            // old title
            if (lastTitleName === "H3"){
                console.log(title)
                TitleH2.append(ulNode);
                //console.log(TitleH2.children())
                var tempNode = TitleH2.children();
                tempNode[0].classList.add("dropdown-toggle");
            }
            console.log(TitleH2)
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
    if (lastTitleName === "H3"){
                TitleH2.append(ulNode);
                //console.log(TitleH2.children())
                var tempNode = TitleH2.children();
                tempNode[0].classList.add("dropdown-toggle");
            }
    article_nav_node.append(TitleH2)
    $("#article_nav").append(article_nav_node);
    for (title of titles){
        tagid = title.id + "tag";
        var new_tag = $("<span></span>",{"id":tagid});
        // don't use title directly!!!!
        // if you use title.append(new_tag) then you will get [object object]
        $("#"+title.id).append(new_tag);

    }
}

function article_createTitleH2(node){
    var topNode = $("<li class=\"list-group-item\"></li>");
    var name = $("<a  href=\"#"+node.id+"tag\">"+node.innerHTML+"</a>");
    topNode.append(name);
    return topNode;
}

function article_createTitleH3(node){
    var retNode = $("<li><a href=\"#"+node.id+"tag\">"+node.innerHTML+"</a></li>")
    return retNode;
}
function reading_num_add(){
    console.log("add reading number")
     $.ajax({

            url: "/api/analysis/articles/" + getAllUrlParams().articleid,
            type: "GET",
        });
}


function article_comment_submit(event){
    event.preventDefault(); 
    var url = "/api/comments";
    if ($('#comment_form').serializeArray()[0].value == "")
        name = "Guest"
    else
        name = $('#comment_form').serializeArray()[0].value
    content = $('#comment_form').serializeArray()[1].value
    console.log("hahaha")
    data_dict = {
        name :name,
        content: content,
        articleid: getAllUrlParams().articleid 
    }
     $.ajax({
            url: url,
            type: "POST",
            data: JSON.stringify(data_dict),
            dataType: "json",
            success: function(data,status){window.location.replace(window.location.search)},
            contentType: "application/json;charset=UTF-8"
        });

}

