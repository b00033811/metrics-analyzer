FROM python:3.5-stretch AS build-env
WORKDIR /usr/src/app
COPY requirements.txt regression.py regression.spec ./
RUN pip install --upgrade pip --upgrade setuptools && \
    pip install -r requirements.txt  && \
    pyinstaller regression.py --hidden-import=pkg_resources.py2_warn --hidden-import=sklearn.utils._cython_blas
RUN echo "Installed App"
FROM gcr.io/distroless/python3
COPY --from=build-env /usr/src/app/dist /usr/src/app/dist
ENTRYPOINT ["/usr/src/app/dist/regression/regression"]