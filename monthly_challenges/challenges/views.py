from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_things= {
    "january":"focus on the boss",
    "february":"go for the weakness",
    "march":"there are enimes near by",
    "april":"there can only be one winner lets go",
    "may":"lets go",
    "june":"idhi pattuko",
    "july":"vango",
    "august":"vennaki vellu ra",
    "september":"Jai bholo ganesh maha raj ki",
    "octber":"dasara is loading",
    "november":"dont stop dancing poonakalu loading",
    "december":None
}


def index(request):
  months=list(monthly_things.keys())
  return render(request,"challenges/index.html",{'month_name':months})
  
  
def monthly_challenges_by_number(request,month):
  month_list=list(monthly_things.keys())
  forward_month=month_list[month-1]
  repath=reverse("month_challenge", args=[forward_month])
  return HttpResponseRedirect(repath)

def monthly_challenges(request,month):
  try:
    challenge_text=monthly_things[month]
    return render(request,'challenges/challenges.html',{
      'month_name':month,
      'month_challenge':challenge_text
    })
  except:
    re_data=render_to_string("404.html")
    return HttpResponseNotFound(re_data)
  
