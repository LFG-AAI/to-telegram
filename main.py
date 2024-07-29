import os
from github import Github
from requests import get
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext

# Inisialisasi bot Telegram
TELEGRAM_BOT_TOKEN = 'RUBAH TOKEN TELE'
GITHUB_ACCESS_TOKEN = 'RUBAH TOKEN GITHUB'

app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Inisialisasi GitHub
g = Github(GITHUB_ACCESS_TOKEN)

# Path lokal untuk Windows
LOCAL_DIRECTORY = 'C:/Users/Administrator/Downloads/getgrass-main/getgrass-main'

# Intro default
intro_text = "Join telegram : https://t.me/allabout_internet\nJangan lupa subscribe dan share"

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Info", callback_data='info')],
        [InlineKeyboardButton("Create Repo", callback_data='create_repo')],
        [InlineKeyboardButton("List Repos", callback_data='list_repos')],
        [InlineKeyboardButton("Delete Repo", callback_data='delete_repo')],
        [InlineKeyboardButton("Edit File", callback_data='edit_file')],
        [InlineKeyboardButton("Repo Link", callback_data='repo_link')],
        [InlineKeyboardButton("List Local Folders", callback_data='list_local_folders')],
        [InlineKeyboardButton("Upload File", callback_data='upload_file')],
        [InlineKeyboardButton("Upload Folder", callback_data='upload_folder')],
        [InlineKeyboardButton("Delete Folder", callback_data='delete_folder')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"{intro_text}\n\nHalo! Pilih perintah yang ingin Anda gunakan:", 
        reply_markup=reply_markup
    )

async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data

    if data == 'info':
        await query.answer()
        await query.message.reply_text(
            "Saya adalah bot Telegram yang memiliki fitur-fitur berikut:\n\n"
            "1. **Info**: Menampilkan informasi tentang bot dan fitur-fitur yang tersedia.\n"
            "2. **Create Repo**: Membuat repositori baru di GitHub dengan nama yang diberikan.\n"
            "3. **List Repos**: Menampilkan daftar repositori Anda di GitHub.\n"
            "4. **Delete Repo**: Menghapus repositori dari GitHub dengan nama yang diberikan.\n"
            "5. **Edit File**: Mengedit konten file di repositori GitHub.\n"
            "6. **Repo Link**: Menampilkan link ke repositori GitHub.\n"
            "7. **List Local Folders**: Menampilkan folder lokal di direktori C:/Users/Administrator/Downloads/getgrass-main/getgrass-main.\n"
            "8. **Upload File**: Mengunggah file dari folder lokal ke repositori GitHub yang dipilih.\n"
            "9. **Upload Folder**: Mengunggah seluruh folder dari folder lokal ke repositori GitHub yang dipilih.\n"
            "10. **Delete Folder**: Menghapus folder dari direktori lokal."
        )
    elif data == 'create_repo':
        await query.answer()
        await query.message.reply_text("Gunakan perintah /create_repo <nama_repo> untuk membuat repositori baru.")
    elif data == 'list_repos':
        await query.answer()
        repos = g.get_user().get_repos()
        repo_names = [repo.name for repo in repos]
        repo_list = '\n'.join(repo_names)
        await query.message.reply_text(f"Daftar repositori:\n{repo_list}")
    elif data == 'delete_repo':
        await query.answer()
        await query.message.reply_text("Gunakan perintah /delete_repo <nama_repo> untuk menghapus repositori.")
    elif data == 'edit_file':
        await query.answer()
        await query.message.reply_text("Gunakan perintah /edit_file <nama_repo> <path_file> <konten_baru> untuk mengedit file.")
    elif data == 'repo_link':
        await query.answer()
        await query.message.reply_text("Gunakan perintah /repo_link <nama_repo> untuk mendapatkan link repositori.")
    elif data == 'list_local_folders':
        await query.answer()
        local_folders = [f.name for f in os.scandir(LOCAL_DIRECTORY) if f.is_dir()]
        files_list = [f.name for f in os.scandir(LOCAL_DIRECTORY) if f.is_file()]
        folder_list = '\n'.join(local_folders)
        file_list = '\n'.join(files_list)
        if folder_list or file_list:
            message = "Folder lokal di C:/Users/Administrator/Downloads/getgrass-main/getgrass-main:\n"
            if folder_list:
                message += f"Folder:\n{folder_list}\n"
            if file_list:
                message += f"File:\n{file_list}\n"
            await query.message.reply_text(message)
        else:
            await query.message.reply_text("Tidak ada folder atau file di C:/Users/Administrator/Downloads/getgrass-main/getgrass-main.")
    elif data == 'upload_file':
        await query.answer()
        await query.message.reply_text("Gunakan perintah /upload_file <nama_repo> <path_file> untuk mengunggah file dari folder lokal.")
    elif data == 'upload_folder':
        await query.answer()
        await query.message.reply_text("Gunakan perintah /upload_folder <nama_repo> <nama_folder> untuk mengunggah folder dari folder lokal.")
    elif data == 'delete_folder':
        await query.answer()
        await query.message.reply_text("Gunakan perintah /delete_folder <nama_folder> untuk menghapus folder.")

async def set_intro(update: Update, context: CallbackContext):
    global intro_text
    new_intro = ' '.join(context.args)
    if not new_intro:
        await update.message.reply_text("Format perintah salah. Gunakan: /set_intro <intro_baru>")
        return
    intro_text = new_intro
    await update.message.reply_text(f"Intro berhasil diubah menjadi:\n{intro_text}")

async def show_intro(update: Update, context: CallbackContext):
    await update.message.reply_text(f"Intro saat ini:\n{intro_text}")

async def create_repo(update: Update, context: CallbackContext):
    if len(context.args) != 1:
        await update.message.reply_text("Format perintah salah. Gunakan: /create_repo <nama_repo>")
        return
    
    repo_name = context.args[0]
    try:
        g.get_user().create_repo(repo_name)
        await update.message.reply_text(f"Repositori '{repo_name}' berhasil dibuat.")
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan saat membuat repositori: {e}")

async def delete_repo(update: Update, context: CallbackContext):
    if len(context.args) != 1:
        await update.message.reply_text("Format perintah salah. Gunakan: /delete_repo <nama_repo>")
        return

    repo_name = context.args[0]
    try:
        repo = g.get_user().get_repo(repo_name)
        repo.delete()
        await update.message.reply_text(f"Repositori '{repo_name}' berhasil dihapus.")
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan saat menghapus repositori: {e}")

async def edit_file(update: Update, context: CallbackContext):
    if len(context.args) < 3:
        await update.message.reply_text("Format perintah salah. Gunakan: /edit_file <nama_repo> <path_file> <konten_baru>")
        return

    repo_name = context.args[0]
    file_path = context.args[1]
    new_content = ' '.join(context.args[2:])

    try:
        repo = g.get_user().get_repo(repo_name)
        contents = repo.get_contents(file_path, ref="main")
        repo.update_file(contents.path, "Update file via Telegram bot", new_content, contents.sha, branch="main")
        await update.message.reply_text(f"File '{file_path}' di repositori '{repo_name}' berhasil diperbarui.")
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan saat memperbarui file: {e}")

async def repo_link(update: Update, context: CallbackContext):
    if len(context.args) != 1:
        await update.message.reply_text("Format perintah salah. Gunakan: /repo_link <nama_repo>")
        return

    repo_name = context.args[0]
    try:
        repo = g.get_user().get_repo(repo_name)
        repo_url = repo.html_url
        await update.message.reply_text(f"Link repositori '{repo_name}': {repo_url}")
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan saat mendapatkan link repositori: {e}")

async def upload_file(update: Update, context: CallbackContext):
    if len(context.args) != 2:
        await update.message.reply_text("Format perintah salah. Gunakan: /upload_file <nama_repo> <path_file>")
        return

    repo_name = context.args[0]
    file_path = context.args[1]
    full_file_path = os.path.join(LOCAL_DIRECTORY, file_path)

    if not os.path.exists(full_file_path) or not os.path.isfile(full_file_path):
        await update.message.reply_text(f"File '{full_file_path}' tidak ditemukan.")
        return

    try:
        repo = g.get_user().get_repo(repo_name)
        with open(full_file_path, 'rb') as f:
            content = f.read()
        repo.create_file(
            f"files/{file_path}",
            f"Upload {file_path}",
            content,
            branch="main"
        )
        await update.message.reply_text(f"File '{file_path}' telah diunggah ke repositori '{repo_name}'.")
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan saat mengunggah file: {e}")

async def upload_folder(update: Update, context: CallbackContext):
    if len(context.args) != 2:
        await update.message.reply_text("Format perintah salah. Gunakan: /upload_folder <nama_repo> <nama_folder>")
        return

    repo_name = context.args[0]
    folder_name = context.args[1]
    folder_path = os.path.join(LOCAL_DIRECTORY, folder_name)

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        await update.message.reply_text(f"Folder '{folder_path}' tidak ditemukan.")
        return

    try:
        repo = g.get_user().get_repo(repo_name)

        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                with open(file_path, 'rb') as f:
                    content = f.read()
                relative_path = os.path.relpath(file_path, folder_path)
                repo.create_file(
                    f"files/{folder_name}/{relative_path}",
                    f"Upload {relative_path}",
                    content,
                    branch="main"
                )
        
        await update.message.reply_text(f"Folder '{folder_name}' telah diunggah ke repositori '{repo_name}'.")
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan saat mengunggah folder: {e}")

async def delete_folder(update: Update, context: CallbackContext):
    if len(context.args) != 1:
        await update.message.reply_text("Format perintah salah. Gunakan: /delete_folder <nama_folder>")
        return

    folder_name = context.args[0]
    folder_path = os.path.join(LOCAL_DIRECTORY, folder_name)

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        await update.message.reply_text(f"Folder '{folder_path}' tidak ditemukan.")
        return

    try:
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(folder_path)
        await update.message.reply_text(f"Folder '{folder_name}' telah dihapus.")
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan saat menghapus folder: {e}")

async def handle_file(update: Update, context: CallbackContext):
    file = await update.message.document.get_file()
    await file.download_to_drive('tempfile')

    try:
        repo_name = 'default-repo'  # Ganti dengan nama repositori default atau implementasikan cara lain untuk memilih repositori
        repo = g.get_repo(repo_name)
        with open('tempfile', 'rb') as f:
            content = f.read()
        repo.create_file(
            f"files/{update.message.document.file_name}",
            f"Upload {update.message.document.file_name}",
            content,
            branch="main"
        )

        os.remove('tempfile')

        await update.message.reply_text("File telah diunggah ke GitHub.")
    
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan saat memproses file: {e}")

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("create_repo", create_repo))
app.add_handler(CommandHandler("delete_repo", delete_repo))
app.add_handler(CommandHandler("edit_file", edit_file))
app.add_handler(CommandHandler("repo_link", repo_link))
app.add_handler(CommandHandler("upload_file", upload_file))
app.add_handler(CommandHandler("upload_folder", upload_folder))
app.add_handler(CommandHandler("delete_folder", delete_folder))
app.add_handler(CommandHandler("set_intro", set_intro))
app.add_handler(CommandHandler("show_intro", show_intro))
app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
