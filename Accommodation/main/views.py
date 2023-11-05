from django.shortcuts import render, redirect
from .models import User, RoomApplication, Room
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, TemplateView, CreateView
from .forms import CustomLoginForm, SignUpForm
from django.urls import reverse, reverse_lazy



# Create your views here.


def home(request):
    return render(request, "main/dashboard.html")


def admin_dashboard(request):
    return render(request, "main/dashboardy.html")


def apply(request):
    if request.method == "POST":
        student_id = request.POST["student_id"]
        student = User.objects.get(id_num=student_id)
        return render(request, "main/student.html", {"student": student})

    return render(request, "main/apply.html")


def apply_room(request, id):
    roomapp = RoomApplication.objects.filter(user__id_num=id).exists()
    if not roomapp:
        student = User.objects.get(id_num=id)
        RoomApplication.objects.create(user=student)
        messages.success(request, "application success")
        return redirect("home")
    messages.error(request, "already applied")
    return redirect("home")


def housing(request):
    return render(request, "main/housing-services.html")


def applications(request):
    applications = RoomApplication.objects.all()
    return render(request, "main/applications.html", {"applications": applications})


def contact(request):
    return render(request, "main/contact.html")


def about(request):
    return render(request, "main/about.html")


def unallocate_rooms(request):
    students = User.objects.filter(room__isnull=False)
    for student in students:
        student.room.available = True
        student.room = None
        student.save()
    previous_url = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_url)


@login_required(login_url="login")
def allocate_rooms(request):
    rooms = Room.objects.filter(available=True)
    print(rooms)
    if rooms:
        disabled = RoomApplication.objects.filter(
            user__status="disabled", reviewed=False
        )
        disabled_count = disabled.count()

        rooms_count = rooms.count()
        i = 0
        if rooms_count <= disabled_count:
            for disabled in disabled:
                room = rooms[i]
                student = disabled.user
                student.room = room
                room.available = False
                room.save()
                student.save()
                disabled.reviewed = True
                disabled.save()
                i += 1
                rooms_count -= 1

        remaining_rooms = rooms_count

        while remaining_rooms > 0:
            east_applicant = (
                RoomApplication.objects.filter(user__province="east", reviewed=False)
                .order_by("?")
                .first()
            )

            if east_applicant:
                student = east_applicant.user
                print(student)
                room = rooms[i]
                student.room = room
                room.available = False
                room.save()
                student.save()
                east_applicant.reviewed = True
                east_applicant.save()
                i += 1
                remaining_rooms -= 1

            if remaining_rooms:
                copperbelt_applicant = (
                    RoomApplication.objects.filter(
                        user__province="copper", reviewed=False
                    )
                    .order_by("?")
                    .first()
                )
                if copperbelt_applicant:
                    student = copperbelt_applicant.user
                    print(student)
                    room = rooms[i]
                    student.room = room
                    student.save()
                    room.available = False
                    room.save()
                    copperbelt_applicant.reviewed = True
                    copperbelt_applicant.save()
                    i += 1
                    remaining_rooms -= 1
            else:
                break

            if remaining_rooms:
                northwest_applicant = (
                    RoomApplication.objects.filter(
                        user__province="northwest", reviewed=False
                    )
                    .order_by("?")
                    .first()
                )
                if northwest_applicant:
                    student = northwest_applicant.user
                    print(student)
                    room = rooms[i]
                    student.room = room
                    student.save()
                    room.available = False
                    room.save()
                    northwest_applicant.reviewed = True
                    northwest_applicant.save()
                    i += 1
                    remaining_rooms -= 1
            else:
                break

            if remaining_rooms:
                north_applicant = (
                    RoomApplication.objects.filter(
                        user__province="north", reviewed=False
                    )
                    .order_by("?")
                    .first()
                )
                if north_applicant:
                    student = north_applicant.user
                    print(student)
                    room = rooms[i]
                    student.room = room
                    student.save()
                    room.available = False
                    room.save()
                    north_applicant.reviewed = True
                    north_applicant.save()
                    i += 1
                    remaining_rooms -= 1
            else:
                break

            if remaining_rooms:
                muchinga_applicant = (
                    RoomApplication.objects.filter(
                        user__province="muchi", reviewed=False
                    )
                    .order_by("?")
                    .first()
                )
                if muchinga_applicant:
                    student = muchinga_applicant.user
                    print(student)
                    room = rooms[i]
                    student.room = room
                    student.save()
                    room.available = False
                    room.save()
                    muchinga_applicant.reviewed = True
                    muchinga_applicant.save()
                    i += 1
                    remaining_rooms -= 1
            else:
                break

            if remaining_rooms:
                central_application = (
                    RoomApplication.objects.filter(
                        user__province="cent", reviewed=False
                    )
                    .order_by("?")
                    .first()
                )
                if central_application:
                    student = central_application.user
                    print(student)
                    room = rooms[i]
                    student.room = room
                    student.save()
                    room.available = False
                    room.save()
                    central_application.reviewed = True
                    central_application.save()
                    i += 1
                    remaining_rooms -= 1
            else:
                break

            if remaining_rooms:
                luap_applicant = (
                    RoomApplication.objects.filter(
                        user__province="luap", reviewed=False
                    )
                    .order_by("?")
                    .first()
                )
                if luap_applicant:
                    student = luap_applicant.user
                    print(student)
                    room = rooms[i]
                    student.room = room
                    student.save()
                    room.available = False
                    room.save()
                    luap_applicant.reviewed = True
                    luap_applicant.save()
                    i += 1
                    remaining_rooms -= 1
            else:
                break

            if remaining_rooms:
                lusaka_applicant = (
                    RoomApplication.objects.filter(user__province="lus", reviewed=False)
                    .order_by("?")
                    .first()
                )
                if lusaka_applicant:
                    student = lusaka_applicant.user
                    print(student)
                    room = rooms[i]
                    student.room = room
                    student.save()
                    room.available = False
                    room.save()
                    lusaka_applicant.reviewed = True
                    lusaka_applicant.save()
                    i += 1
                    remaining_rooms -= 1
            else:
                break

            if remaining_rooms:
                southern_applicant = (
                    RoomApplication.objects.filter(
                        user__province="south", reviewed=False
                    )
                    .order_by("?")
                    .first()
                )
                if southern_applicant:
                    student = southern_applicant.user
                    print(student)
                    room = rooms[i]
                    student.room = room
                    student.save()
                    room.available = False
                    room.save()
                    southern_applicant.reviewed = True
                    southern_applicant.save()
                    i += 1
                    remaining_rooms -= 1
            else:
                break

            if remaining_rooms:
                western_applicant = (
                    RoomApplication.objects.filter(
                        user__province="west", reviewed=False
                    )
                    .order_by("?")
                    .first()
                )
                if western_applicant:
                    student = western_applicant.user
                    print(student)
                    room = rooms[i]
                    student.room = room
                    student.save()
                    room.available = False
                    room.save()
                    western_applicant.reviewed = True
                    western_applicant.save()
                    i += 1
                    remaining_rooms -= 1
            else:
                break

        allocated_student_list = User.objects.filter(room__isnull=False)
        print(allocated_student_list)
        return render(
            request,
            "main/allocated_list.html",
            {"allocated_student_list": allocated_student_list},
        )
    else:
        messages.error(request, "rooms Already allocated")
        return redirect("dashboard")


def view_allocated(request):
    allocated_student_list = User.objects.filter(room__isnull=False)
    return render(
        request,
        "main/allocated_list.html",
        {"allocated_student_list": allocated_student_list},
    )


from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.pagesizes import letter


def generate_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=allocationlist.pdf"
    doc = SimpleDocTemplate(response, pagesize=letter)
    story = []
    data = []
    allocated_student_list = User.objects.filter(room__isnull=False)
    for student in allocated_student_list:
        data.append([student.name, student.id_num, student.room])
    table = Table(data)
    story.append(table)
    doc.build(story)

    return response


class CustomLoginView(TemplateView):
    form_class = CustomLoginForm
    template_name = "main/login.html"

    def post(self, *args, **kwargs):
        data = self.request.POST
        id_num = data.get("username")
        password = data.get("password")

        user = authenticate(self.request, username=id_num, password=password)
        if user:
            login(self.request, user)
            if user.user_role == "admin":
                return redirect("dashboard")
            else:
                return redirect('home')

        else:
            return render(
                self.request,
                self.template_name,
                {"error_message": "invalid credentials", "form": self.form_class()},
            )

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "main/signup.html"
    success_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})


def logout_user(request):
    logout(request)
    return redirect("home")
