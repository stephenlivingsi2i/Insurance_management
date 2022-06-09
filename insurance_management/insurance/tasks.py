import smtplib
from datetime import date, datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail
from rest_framework.response import Response

from employee.models import Employee
from insurance.models import Insurance
from insurance.serializer import InsuranceSerializer
from insurance_management import settings


# @shared_task(bind=True)
# def send_mails(self):
#     try:
#         send_mail(
#             subject="Insurance renewal",
#             message="message",
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=["livings.be@gmail.com"],
#         )
#         is_mail_sent = True
#     except smtplib.SMTPResponseException as mail_error:
#         is_mail_sent = False
#     return is_mail_sent


@shared_task(bind=True)
def remind_insurances(self):

    try:
        mail_server = smtplib.SMTP('smtp.gmail.com', 587)
        mail_server.starttls()
        mail_server.login("subscriptionforyou45@gmail.com", "just$for$demo")
        today_date = date.today()
        today_date = today_date+timedelta(days=2)
        today_date = today_date.strftime('%Y-%m-%d')
        reminder_list = Insurance.objects.filter(
            renewal_date=today_date)
        for insurance in reminder_list:
            # name = insurance["holder_name"]
            # insurance_number = insurance["insurance_number"]
            # email = Employee.objects.get(pk=insurance['employee']).email
            name = insurance.holder_name
            insurance_number = insurance.insurance_number
            email = insurance.employee.email
            message = f"Hi, {name} , your insurance plan {insurance_number} " \
                      f"expired within two days"
            mail_server.sendmail("subscriptionforyou45@gmail.com", email, message)

        # return Response("mail sent successfully")
        mail_server.quit()
    except smtplib.SMTPResponseException as mail_error:
        pass


