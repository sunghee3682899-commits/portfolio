import os
from flask import Blueprint, render_template
from flask import current_app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # image 폴더에서 이미지 파일 자동으로 불러오기
    image_folder = os.path.join(current_app.root_path, 'static', 'image')
    images = [
        f for f in os.listdir(image_folder)
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))
    ]
    return render_template('main.html', images=images)