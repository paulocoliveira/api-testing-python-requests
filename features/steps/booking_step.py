import os
import sys
import json

PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from hamcrest import assert_that, is_
from common.apis.booking_api import create_booking, delete_bookings, get_all_bookings
from common.models import Booking

@when(u'I create a booking')
def create_booking_impl(context):
    for row in context.table:
        booking = Booking(row['first_name'], row['last_name'], row['total_price'], row['deposit_paid'], row['checkin'], row['checkout'], row['additional_needs'])
        context.booking = booking
        context.response = create_booking(context, booking)
        assert_that(context.response.status_code, is_(201))

@given(u'Booking list is empty')
def delete_bookings_impl(context):
    context.response = delete_bookings(context)
    assert_that(context.response.status_code, is_(204))

@when(u'I get the list of bookings')
def get_all_bookings_impl(context):
    context.response = get_all_bookings(context)
    assert_that(context.response.status_code, is_(200))

@then(u'I verify that the booking "{booking_id}" was registered')
def step_impl(context, booking_id):
    assert_that(context.booking.first_name, is_(context.response.json()[booking_id]['first_name']))
    assert_that(context.booking.last_name, is_(context.response.json()[booking_id]['last_name']))
    assert_that(context.booking.total_price, is_(context.response.json()[booking_id]['total_price']))
    assert_that(context.booking.deposit_paid, is_(context.response.json()[booking_id]['deposit_paid']))
    assert_that(context.booking.checkin, is_(context.response.json()[booking_id]['checkin']))
    assert_that(context.booking.checkout, is_(context.response.json()[booking_id]['checkout']))
    assert_that(context.booking.additional_needs, is_(context.response.json()[booking_id]['additional_needs']))