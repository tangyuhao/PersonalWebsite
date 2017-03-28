$(document).ready(function() {
    $.getJSON("/api/nav/topnavbar",topnavbar_handler)

});
function topnavbar_handler(data){
    console.log(data);

    var blogGroup = data.Blog;
    //console.log(blogGroup);
    var photography = data.Photography;
    var photographyList = $("<ul></ul>",{"class":"dropdown-menu"});
    for (var item of photography){
        photographyList.append("<li><a href=\"/album?albumid=" + item.albumid + "\">"+
            item.title.toUpperCase() + "</a></li>");
    }
    /******** choose whether to show photography menu ********/
    // choose below to show photograph
    //$("#nav-photography").after(photographyList)
    // choose below to delete photograph
    $("#nav-photography").remove()
    /* *********************************************** */

    keys = Object.keys(blogGroup).sort();
    keys.splice(keys.indexOf("Others"),1);
    keys.push("Others");
    //console.log(keys);

    var blogGroupList = $("<ul></ul>",{"class":"dropdown-menu"});
    for (var key of keys ){
        // console.log(key);
        var blogs = blogGroup[key];
        var blogList = $("<li></li>",{"class":"dropdown"});
        var subList = $("<ul></ul>",{"class":"dropdown-menu"});
        blogList.append("<a class=\"dropdown-toggle\" href=\"#\">"+key.toUpperCase()+"</a>")
        // console.log(blogs)

        for (var item in blogs){
            //console.log( blogs[item]);
            subList.append("<li><a href=\"/blog?blogid=" +  blogs[item].blogid + "\">"+
            blogs[item].title.toUpperCase() + "</a></li>");
        }
        blogList.append(subList);
        blogGroupList.append(blogList);
    }
    $("#nav-blog").after(blogGroupList);


    var addActiveClass  = false;
        //jQuery("#topMain a.dropdown-toggle").bind("click", function(e) 
        jQuery("#topMain a.dropdown-toggle").bind("click", function(e) {
            
            if(jQuery(this).attr('href') == "#") {
                e.preventDefault();
            }

            addActiveClass = jQuery(this).parent().hasClass("resp-active");
            jQuery("#topMain").find(".resp-active").removeClass("resp-active");

            if(!addActiveClass) {
                jQuery(this).parents("li").addClass("resp-active");
            }

            return;

        });

}