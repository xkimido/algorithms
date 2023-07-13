def solution(chicken):
    coupons = chicken
    total_chicken = 0
    service_chicken = 0 

    while coupons >= 10:
        service = coupons // 10

        coupons -= service * 10

        service_chicken += service

        order = service + coupons

        total_chicken += order

        coupons = order

    return service_chicken