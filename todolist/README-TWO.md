# Tugas 6: Javascript dan Ajax

> Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

---

> [Deployed Web](https://ferryhusnil-pbp-assignment.herokuapp.com/todolist/)

---

1. **Asynchronous vs Synchronous Programming**

Asynchronous programming adalah suatu paradigma programming yang memungkinkan untuk mengeksekusi lebih dari satu routine secara paralel. Berbeda dengan Synchronous programming yang hanya terdiri dari satu routine saja. Sehingga untuk mengerjakan lebih dari satu fungsi, fungsi berikutnya hanya bisa dijalankan ketika fungsi pertama sudah selesai

2. **Event-driven Programming**

Event adalah "interrupt" atau dengan kata lain sinyal yang diberikan kepada sebuah current proses untuk dihandle oleh current proses tersebut. Dengan menggunakan event-driven programming kita bisa membuat logic dan fungsionalitas program yang lebih kompleks dan terarah. misalkan ketika terjadi event A, maka execute proses B dan proses C. Lebih jauh lagi, kita bisa membuat program kita lebih interaktif seperti event dari click.

3. **Async AJAX**

    1. Ketika terjadi event, maka JavaScript akan membuat object XHR baru.
    2. objek XHR ini bertugas untuk mengirim HTTP request ke server, dan kemudian mendapatkan response dari server
    3. Setelah mendapatkan data dari response, data web akan diperbarui secara interaktif tanpa memerlukan reload kembali halaman tersebut

4. **Implementasi**

    - Import jquery cdn
    ```html
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    ```
    - Menulis semua script yang diperlukan, `fetchTask()` untuk mendapatkan data json, `submitTask()` untuk mensubmit task baru dari form, `showTask()` untuk menampilkan data di page HTML.
    ```html
        <script>
    $(document).ready(function () {
        fetchTask();
        submitTask();
    });

    function fetchTask() {
        $.get(window.location.href + "json", showTask);
    }

    function showTask(data) {
        const placeholder = $("#show-task");
        console.log(data);
        placeholder.empty();

        if (data != undefined && data.length > 0) {
        data.forEach(function (task) {
            placeholder.append(`<div
        class="card w-full bg-neutral-800 shadow-xl transform transition hover:scale-105 hover:bg-opacity-95 duration-200"
    >
        <div class="card-body">
        <div class="card-actions justify-end">
            <label
            for="modal-close-${task.pk}"
            class="btn btn-square btn-sm modal-button"
            >
            <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
            >
                <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0"
                />
            </svg>
            </label>
        </div>
        <h2 class="card-title text-2xl md:text-3xl">${task.fields.title}</h2>
        <p class="text-xs md:text-sm">${task.fields.date}</p>
        <p class="text-sm md:text-lg break-words">${task.fields.description}</p>
        <div class="card-actions justify-end">
            ${
            task.fields.is_finished
                ? `<a
            href="/todolist/update-task/${task.pk}"
            role="button"
            class="btn btn-primary btn-sm text-sm md:btn-md md:text-base"
            >done!</a
            >`
                : `<a
            href="/todolist/update-task/${task.pk}"
            role="button"
            class="btn btn-sm text-sm md:btn-md md:text-base"
            >mark as done!</a
            >`
            }
        </div>
        </div>
    </div>
    <input type="checkbox" id="modal-close-${task.pk}" class="modal-toggle" />
    <div class="modal modal-middle">
        <div class="modal-box">
        <div class="flex flex-row justify-end">
            <label
            for="modal-close-${task.pk}"
            class="btn btn-sm btn-square right-2 top-2"
            ><svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
                /></svg
            ></label>
        </div>

        <h3 class="text-lg font-bold">Your task will permanently deleted</h3>
        <p class="py-4">are you sure?</p>
        <div class="modal-action mt-10">
            <a
            href="/todolist/delete-task/${task.pk}"
            class="btn btn-warning hover:bg-opacity-70"
            >delete</a
            >
            <label
            for="modal-close-${task.pk}"
            class="btn btn-primary hover:bg-opacity-70"
            >cancel</label
            >
        </div>
        </div>
    </div>`);
        });
        } else {
        placeholder.append(
            `<p id="empty-task-notice" class="text-2xl text-slate-700 font-bold text-center my-20"> Kamu belum punya todo list, yukk mulai buat!</p>`
        );
        }

        function submitTask() {
        $("#submit-task").submit(function (e) {
            console.log(e);
            e.preventDefault();
            var actionURL = "/todolist/add";
            var formData = $(this).serialize();
            $.ajax({
            url: actionURL,
            type: "POST",
            data: formData,
            dataType: "json",
            success: (data) => {
                $("#close-task-modal").click();

                // console.log(data);
                showTask(data);
            },
            error: (error) => {
                console.log(error);
                alert("Error!");
            },
            });
        });
        }
    }
    </script>
    ```
    - membuat path baru di urls untuk mendapatkan data json dan menambahkan data ajax
    ```python
        path("json", show_todolist_json, name="show_todolist_json"),
        path("add", create_task_ajax, name="create_task_json"),
    ```

    - membuat logic app pada views.py untuk menghandle HTTP request di atas
    ```python
    @login_required(login_url="/todolist/login")
    def show_todolist_json(request):
        data = Task.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    @login_required(login_url="/todolist/login")
    def create_task_ajax(request):
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = auth_models.User.objects.get(pk=request.user.id)
                task.save()
                tasks = Task.objects.filter(user=request.user)
                return HttpResponse(serializers.serialize("json", tasks), content_type="application/json")
        else:
            form = TaskForm()
        context = {"form": form}
        return HttpResponse("only POST method allowed!")
    ```
