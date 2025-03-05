FROM tyronextian/debian_python_base:3.10.13

# 把根目录的requirements.txt拷贝到这来再做镜像
COPY requirements.txt /tmp

ARG code_dir="/code"
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:$code_dir"

WORKDIR $code_dir

RUN pip install --no-cache-dir -r  /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple &&  \
    rm -rf /tmp/requirements.txt && apt clean && rm -rf /var/lib/apt/lists/*


COPY . $code_dir

CMD ["gunicorn", "-c", "gunicorn.conf.py", "server:create_app()"]