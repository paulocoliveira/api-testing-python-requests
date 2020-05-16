Feature: Booking
        
    Scenario: TC_BOO_001 - Verify that it is possible to create a booking
        Given Booking list is empty
        When I create a booking
            |first_name |last_name |total_price |deposit_paid |checkin    |checkout   |additional_needs    |
            |Tom        |Cruise    |1150.00     |500.00       |2020-06-01 |2020-06-03 |With Children       |
            |Angelina   |Jolie     |12500.00    |7500.00      |2020-05-30 |2020-06-12 |King Size Bed       |
            |Emma       |Watson    |5000.00     |2100.00      |2020-06-10 |2020-06-16 |With Magic Suitcase |
