from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 
from django.shortcuts import redirect
seasons = {
    "fall": {
        "title": "🍁 Fall",
        "body": "The air turns crisp, leaves ablaze in fiery hues, as we welcome cozy sweaters and warm pumpkin spice everything.",
    },
    "winter": {
        "title": "❄️ Winter",
        "body": "A hush falls over the world, blanketed in white, perfect for snuggling by the fire with a good book and a steaming cup of cocoa.",
    },
    "spring": {
        "title": "🌱 Spring",
        "body": "The earth awakens with a burst of life; vibrant flowers bloom, and the sweet scent of new beginnings fills the refreshing air.",
    },
    "summer": {
        "title": "☀️ Summer",
        "body": "Long, sun-drenched days stretch into balmy nights, inviting lazy afternoons, beach trips, and the joy of simple, carefree adventures.",
    },
}
def blog_home(request):
    return render(request, "blog/home.html", context={"seasons": seasons})

def contact_us(request):
    return render(request, "blog/contact_us.html")


def blog_season(request, season: str):
    content = seasons.get(season)
    if content is None:
        status = 404
    else:
        status = 200
    return render(request, "blog/season.html", context={"season": content}, status= status)

def blog_season_by_number(request, season:int):
    season_keys = list(seasons.keys())

    if season >= len(season_keys):
        return render(request, "blog/season.html", status = 404)     
    season_key  = season_keys[season]

    return redirect("blog-season" , season = season_key)
