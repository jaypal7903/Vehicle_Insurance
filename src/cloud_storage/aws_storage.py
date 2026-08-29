import os
import sys
import pickle

from io import StringIO
from typing import Union, List

import pandas as pd

from botocore.exceptions import ClientError
from mypy_boto3_s3.service_resource import Bucket

from src.configuration.aws_connection import S3Client
from src.exception import MyException
from src.logger import logging


class SimpleStorageService:
    """
    A class for interacting with AWS S3 storage.
    Provides methods for file management, data uploads,
    and data retrieval from S3 buckets.
    """

    def __init__(self):
        """
        Initializes SimpleStorageService with S3 resource and client.
        """

        s3_client = S3Client()

        self.s3_resource = s3_client.s3_resource
        self.s3_client = s3_client.s3_client

    def s3_key_path_available(
        self,
        bucket_name: str,
        s3_key: str
    ) -> bool:
        """
        Checks whether a specified S3 key exists in a bucket.
        """

        try:
            bucket = self.get_bucket(bucket_name)

            file_objects = [
                file_object
                for file_object in bucket.objects.filter(
                    Prefix=s3_key
                )
            ]

            return len(file_objects) > 0

        except Exception as e:
            raise MyException(e, sys) from e

    @staticmethod
    def read_object(
        object_name,
        decode: bool = True,
        make_readable: bool = False
    ) -> Union[StringIO, str, bytes]:
        """
        Reads an S3 object.

        Args:
            object_name: S3 ObjectSummary/Object.
            decode: Whether to decode bytes into string.
            make_readable: Whether to convert content to StringIO.

        Returns:
            Object content.
        """

        logging.info(
            "Entered read_object method of SimpleStorageService class."
        )

        try:
            body = object_name.get()["Body"].read()

            if decode:
                body = body.decode("utf-8")

            if make_readable:
                body = StringIO(body)

            logging.info(
                "Exited read_object method of SimpleStorageService class."
            )

            return body

        except Exception as e:
            raise MyException(e, sys) from e

    def get_bucket(self, bucket_name: str) -> Bucket:
        """
        Retrieves an S3 bucket object.
        """

        logging.info(
            "Entered get_bucket method of SimpleStorageService class."
        )

        try:
            bucket = self.s3_resource.Bucket(bucket_name)

            logging.info(
                "Exited get_bucket method of SimpleStorageService class."
            )

            return bucket

        except Exception as e:
            raise MyException(e, sys) from e

    def get_file_object(
        self,
        filename: str,
        bucket_name: str
    ) -> Union[List[object], object]:
        """
        Retrieves S3 object(s) based on filename.
        """

        logging.info(
            "Entered get_file_object method of SimpleStorageService class."
        )

        try:
            bucket = self.get_bucket(bucket_name=bucket_name)

            file_objects = [
                file_object
                for file_object in bucket.objects.filter(
                    Prefix=filename
                )
            ]

            if not file_objects:
                raise FileNotFoundError(
                    f"File '{filename}' not found "
                    f"in bucket '{bucket_name}'."
                )

            file_objs = (
                file_objects[0]
                if len(file_objects) == 1
                else file_objects
            )

            logging.info(
                "Exited get_file_object method of SimpleStorageService class."
            )

            return file_objs

        except Exception as e:
            raise MyException(e, sys) from e

    def load_model(
        self,
        model_name: str,
        bucket_name: str,
        model_dir: str = None
    ) -> object:
        """
        Loads a serialized model from an S3 bucket.
        """

        try:
            model_file = (
                f"{model_dir}/{model_name}"
                if model_dir
                else model_name
            )

            file_object = self.get_file_object(
                model_file,
                bucket_name
            )

            model_obj = self.read_object(
                file_object,
                decode=False
            )

            model = pickle.loads(model_obj)

            logging.info(
                "Production model loaded from S3 bucket."
            )

            return model

        except Exception as e:
            raise MyException(e, sys) from e

    def create_folder(
        self,
        folder_name: str,
        bucket_name: str
    ) -> None:
        """
        Creates a folder in the specified S3 bucket.
        """

        logging.info(
            "Entered create_folder method of SimpleStorageService class."
        )

        try:
            self.s3_resource.Object(
                bucket_name,
                folder_name
            ).load()

            logging.info(
                f"Folder '{folder_name}' already exists."
            )

        except ClientError as e:

            if e.response["Error"]["Code"] == "404":

                folder_obj = folder_name.rstrip("/") + "/"

                self.s3_client.put_object(
                    Bucket=bucket_name,
                    Key=folder_obj
                )

            else:
                raise MyException(e, sys) from e

        except Exception as e:
            raise MyException(e, sys) from e

    def upload_file(
        self,
        from_filename: str,
        to_filename: str,
        bucket_name: str,
        remove: bool = True
    ) -> None:
        """
        Uploads a local file to S3.
        """

        logging.info(
            "Entered upload_file method of SimpleStorageService class."
        )

        try:
            logging.info(
                f"Uploading {from_filename} "
                f"to {to_filename} in {bucket_name}"
            )

            self.s3_resource.meta.client.upload_file(
                from_filename,
                bucket_name,
                to_filename
            )

            logging.info(
                f"Uploaded {from_filename} "
                f"to {to_filename} in {bucket_name}"
            )

            if remove:
                os.remove(from_filename)

                logging.info(
                    f"Removed local file {from_filename}."
                )

            logging.info(
                "Exited upload_file method of SimpleStorageService class."
            )

        except Exception as e:
            raise MyException(e, sys) from e

    def upload_df_as_csv(
        self,
        data_frame: pd.DataFrame,
        local_filename: str,
        bucket_filename: str,
        bucket_name: str
    ) -> None:
        """
        Uploads a DataFrame as CSV to S3.
        """

        logging.info(
            "Entered upload_df_as_csv method of SimpleStorageService class."
        )

        try:
            data_frame.to_csv(
                local_filename,
                index=False,
                header=True
            )

            self.upload_file(
                local_filename,
                bucket_filename,
                bucket_name
            )

            logging.info(
                "Exited upload_df_as_csv method of SimpleStorageService class."
            )

        except Exception as e:
            raise MyException(e, sys) from e

    def get_df_from_object(
        self,
        object_
    ) -> pd.DataFrame:
        """
        Converts an S3 object into a pandas DataFrame.
        """

        logging.info(
            "Entered get_df_from_object method of SimpleStorageService class."
        )

        try:
            content = self.read_object(
                object_,
                make_readable=True
            )

            df = pd.read_csv(
                content,
                na_values="na"
            )

            logging.info(
                "Exited get_df_from_object method of SimpleStorageService class."
            )

            return df

        except Exception as e:
            raise MyException(e, sys) from e

    def read_csv(
        self,
        filename: str,
        bucket_name: str
    ) -> pd.DataFrame:
        """
        Reads a CSV file from S3 and converts it to a DataFrame.
        """

        logging.info(
            "Entered read_csv method of SimpleStorageService class."
        )

        try:
            csv_obj = self.get_file_object(
                filename,
                bucket_name
            )

            df = self.get_df_from_object(csv_obj)

            logging.info(
                "Exited read_csv method of SimpleStorageService class."
            )

            return df

        except Exception as e:
            raise MyException(e, sys) from e