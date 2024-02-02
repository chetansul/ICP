
from core.models import drugs,result
import twilio.rest
from celery import shared_task
from django.core.mail import send_mail
from pharma import settings
from datetime import date,timedelta
from django.core.mail import EmailMultiAlternatives

@shared_task(bind=True)
def send_mail_func(self):
    # Get all instances of the result model
    all_results = result.objects.all()

    for res in all_results:
        alert_dates_dict = {}

        # Calculate alert dates based on stability category
        print(f"Processing result for drug: {res.drug} with stabilities: {res.stabilities.all()}")
        for stability in res.stabilities.all():
            stability_name = stability.stab_name.lower().strip()
            print(stability_name)
            print("\n\n")

            if stability_name == 'accelerated':
                alert_dates_dict[stability_name] = [res.alert_date + timedelta(days=30 * i) for i in [1, 2, 3, 6]]
            elif stability_name == 'intermediate':
                alert_dates_dict[stability_name] = [res.alert_date + timedelta(days=30 * i) for i in [1, 3, 6, 9, 12]]
            elif stability_name == 'longterm':
                alert_dates_dict[stability_name] = [res.alert_date + timedelta(days=30 * i) for i in [1, 3, 6, 9, 12, 18, 24]]
            else:
                alert_dates_dict[stability_name] = []

            print(f"Alert dates for stability {stability_name}: {alert_dates_dict[stability_name]}")
        # If there are no alert dates for the stability category, skip to the next result
        if not alert_dates_dict:
            print("Skipping due to empty alert_dates")
            continue

        current_date = date.today()
        print (alert_dates_dict)
        print("\n\n\n")
        for stability_name, alert_dates in alert_dates_dict.items():
            for alert_date in alert_dates:
                if current_date == alert_date or current_date == (alert_date - timedelta(days=1)) or current_date == (alert_date + timedelta(days=1)):
                    user_email = res.drug.email  # Assuming a OneToOneField to drugs
                    alert_interval = (alert_date - res.alert_date).days // 30
                    mail_subject = f"Alert for {alert_interval}-month {stability_name} stability"

                    # Concatenate stability names
                    all_stabilities = ', '.join([stability.stab_name for stability in res.stabilities.all()])

                    message = f"""
                    <h1>Dear {res.drug.Name},</h1>
                    <h2>Alert for {alert_interval}-month {stability_name} stability</h2>
                    <table border="1">
                    <tr>
                        <th>Product Name</th>
                        <th>Batch No.</th>
                        <th>Mfg Date</th>
                        <th>Stabilities</th>
                        <!-- Add more columns as needed -->
                    </tr>
                    <tr>
                        <td>{res.drug.Productname}</td>
                        <td>{res.drug.batch}</td>
                        <td>{res.drug.mfg}</td>
                        <td>{all_stabilities}</td>
                        <!-- Add more cells as needed -->
                    </tr>
                    </table>
                    """

                    msg = EmailMultiAlternatives(
                        subject=mail_subject,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[user_email],
                    )
                    msg.attach_alternative(message, "text/html")
                    msg.send(fail_silently=True)
    return "done"


@shared_task(bind=True)
def send_sms(self):
    account_sid = "AC3accb0615c53343f9564326db68f9c0d"
    auth_token = "ea7f23e4f50712e47257d4b295c575fe"

    # Create a Twilio client
    client = twilio.rest.Client(account_sid, auth_token)

    # Get all instances of the result model
    all_results = result.objects.all()

    for res in all_results:
        alert_dates_dict = {}

        # Calculate alert dates based on stability category
        print(f"Processing result for drug: {res.drug} with stabilities: {res.stabilities.all()}")
        for stability in res.stabilities.all():
            stability_name = stability.stab_name.lower().strip()
            print(stability_name)
            if stability_name == 'accelerated':
                alert_dates_dict[stability_name] = [res.alert_date + timedelta(days=30 * i) for i in [1, 2, 3, 6]]
            elif stability_name == 'intermediate':
                alert_dates_dict[stability_name] = [res.alert_date + timedelta(days=30 * i) for i in [1, 3, 6, 9, 12]]
            elif stability_name == 'longterm':
                alert_dates_dict[stability_name] = [res.alert_date + timedelta(days=30 * i) for i in [1, 3, 6, 9, 12, 18, 24]]
            else:
                alert_dates_dict[stability_name] = []

            print(f"Alert dates for stability {stability_name}: {alert_dates_dict[stability_name]}")

        # If there are no alert dates for the stability category, skip to the next result
        if not alert_dates_dict:
            print("Skipping due to empty alert_dates")
            continue

        current_date = date.today()

        # If current date is one day before or on the alert date, send SMS
        for stability_name, alert_dates in alert_dates_dict.items():
            for alert_date in alert_dates:
                if current_date == alert_date or current_date == (alert_date - timedelta(days=1)) or current_date == (alert_date + timedelta(days=1)):
                    user_phone_number = res.drug.mobile  # Replace with the actual field
                    alert_interval = (alert_date - res.alert_date).days // 30
                    body = f"Alert for {alert_interval}-month {stability_name} stability: {res.drug.Productname}"

                    message = client.messages.create(
                        to="+91"+str(user_phone_number),
                        from_="+14844942570",
                        body=body
                    )


    return "done"




'''


            mail_subject = f"Alert for {alert_interval}-month stability"
            to_email = user_email

            send_mail(
                subject=mail_subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[to_email],
                fail_silently=True,
            )
def send_mail_func(self):
    #operation
    all_drugs= drugs.objects.all()
    users = [drug.email for drug in all_drugs]
    all_dates=result.objects.all()
    dates=[result.alert_date for da in all_dates]
    current_date = date.today()

    for d in dates:
        if d==current_date: 
            for user in users:
                mail_subject ="hey testing in going on of perodic task"
                message="working"
                to_email = user

                send_mail(
                    subject=mail_subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[to_email],
                    fail_silently=True,
                    
                )
    
    return "done"
    ---------------

    @shared_task(bind=True)
def send_mail_func(self):
    # Operation
    current_date = date.today()
    #all_drugs = result.objects.select_related('drug').all()
   # users = [drug.email for drug in all_drugs]

    all_results = result.objects.select_related('drug').all()

    for res in all_results:
        alert_date = res.alert_date

        # Compare year, month, and day separately
        if alert_date.year == current_date.year and alert_date.month == current_date.month and alert_date.day == current_date.day:
            user_email = res.drug.email
            mail_subject = "Hey, working"
            message = "passed"
            to_email = user_email

            send_mail(
                    subject=mail_subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[to_email],
                    fail_silently=True,
                )

    return "done"

    --------------------------------

    @shared_task(bind=True)
def send_sms(self):
    account_sid = "AC3accb0615c53343f9564326db68f9c0d"
    auth_token = "49d8a46bc6ea246c9044eb2b2edc8caa"

    # Create a Twilio client
    client = twilio.rest.Client(account_sid, auth_token)
    message = client.messages.create(
    to="+919106361197",
    from_="+14844942570",
    body="new perodic task"
    )

    return "done"


'''