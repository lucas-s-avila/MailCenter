FROM python:3.8 as builder-img
RUN pip install --no-cache-dir --upgrade pip

RUN python3.8 -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.8 as web-img

COPY --from=builder-img /venv /venv

ENV PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/venv
ENV PATH="/venv/bin:$PATH"

WORKDIR /MailCenter

ADD . .

RUN mkdir "staticfiles"