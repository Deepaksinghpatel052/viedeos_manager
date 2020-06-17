from django.shortcuts import render,get_object_or_404
from django.views import generic
from videos.models import VsVideos
from videos.filters import VideosFilter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from account.models import VsUsers
from categorys_and_reatings.models import VsCategory
from system_setting.models import VsSystemSettings
from favourite_videos.models import VsFavourite
from videos.models import VsVideos,VsComments,VsRating
from django.db.models import Count
from django.template.defaulttags import register
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
# Create your views here.

@register.filter(name='get_vote_video')
def get_vote_video(video_id):
    status = "Video removed successfully."
    video = None
    if VsVideos.objects.filter(id=video_id).filter(Publich_Status=True).exists():
        video = get_object_or_404(VsVideos,id=video_id,Publich_Status=True)
    user_data = {"video":video}
    return render_to_string("web/my_viewos/voted_videos.html",user_data)


def RemoveVIdeo(request,video_id):
    status = "Video Removed Successfully."
    if video_id:
        if VsVideos.objects.filter(Videos_id=video_id).exists():
            VsVideos.objects.filter(Videos_id=video_id).delete()
    return JsonResponse({"status":status})

@method_decorator(login_required , name="dispatch")
class MyVideosView(generic.ListView):
    template_name = "web/my_viewos/my_videos.html"

    def get_queryset(self):
        Created_By = get_object_or_404(VsUsers, user=self.request.user)
        if Created_By.Type.lower()=="performer":
            get_cate_ins = None
            if "types" in self.kwargs:
                if VsCategory.objects.filter(Slug=self.kwargs["types"]).exists():
                    get_cate_ins = get_object_or_404(VsCategory,Slug=self.kwargs["types"])
            
            get_my_videos = None

            if get_cate_ins is None:
                if VsVideos.objects.filter(Created_By=Created_By).filter(Publich_Status=True).exists():
                    get_my_videos = VsVideos.objects.filter(Created_By=Created_By).filter(Publich_Status=True).order_by("-Created_date")
            else:
                if VsVideos.objects.filter(Created_By=Created_By).filter(Categoryes=get_cate_ins).filter(Categoryes = get_cate_ins).filter(Publich_Status=True).exists():
                    get_my_videos = VsVideos.objects.filter(Created_By=Created_By).filter(Categoryes=get_cate_ins).filter(Categoryes = get_cate_ins).filter(Publich_Status=True).order_by("-Created_date")
            return get_my_videos
        else:
            get_cate_ins = None
            if "types" in self.kwargs:
                if VsCategory.objects.filter(Slug=self.kwargs["types"]).exists():
                    get_cate_ins = get_object_or_404(VsCategory,Slug=self.kwargs["types"])

            get_my_videos = None
            if get_cate_ins is None:
                if VsFavourite.objects.filter(VsUser=Created_By).exists():
                    get_my_videos = VsFavourite.objects.filter(VsUser=Created_By)
            else:
                if VsFavourite.objects.filter(VsUser=Created_By).filter(Video__Categoryes=get_cate_ins).exists():
                    get_my_videos = VsFavourite.objects.filter(VsUser=Created_By).filter(Video__Categoryes=get_cate_ins)
            return get_my_videos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Category = None
        if VsCategory.objects.filter(Status=True).exists():
            Category = VsCategory.objects.filter(Status=True).order_by('Title')
        context["Category"] = Category
        Created_By = get_object_or_404(VsUsers, user=self.request.user)
        context["count"]  =  VsVideos.objects.filter(Created_By=Created_By,Publich_Status=True).order_by("-Created_date").count()
        system_settings = VsSystemSettings.objects.all().first()
        context["system_upload_limit"] = system_settings.No_of_videos_uploaded_by_one_account
        
        my_fave = None

        if "types" in self.kwargs:
            context["type"] = self.kwargs['types']
            get_cate_ins = None
            if VsCategory.objects.filter(Slug=self.kwargs["types"]).exists():
                get_cate_ins = get_object_or_404(VsCategory,Slug=self.kwargs["types"])
            
            if VsRating.objects.values('Video').filter(User=Created_By).filter(Video__Categoryes=get_cate_ins).filter(Status=True).exists():
                my_fave = VsRating.objects.values('Video').filter(User=Created_By).filter(Video__Categoryes=get_cate_ins).filter(Status=True).annotate(total=Count('id'))
        else:
            if VsRating.objects.values('Video').filter(User=Created_By).filter(Status=True).exists():
                my_fave = VsRating.objects.values('Video').filter(User=Created_By).filter(Status=True).annotate(total=Count('id'))
        context["my_fave"] = my_fave
        print(my_fave) 
        return context

