function getMin($s){
    $stack = array();
    #count = 0;

    for ($i = 0; $i < strlen($s); $i++) {
        $char = $s[$i];
        if ($char == '(') {
            array_push($stack, '(');
        } elseif ($char == ')') {
            if (!empty($stack)) {
                array_pop($stack);  
            } else {
                $count++;  
            }
        }
    }

    $count += count($stack);
    return $count;
}


def weatherStation(keyword):
query_data = 'https://jsonmock.hackerrank.com/api/weather/'
try:
        response = requests.get(query_data)
        data = response.json()

        filtered_data = []

        for city in data['cities']:
            if keyword.lower() in city['name'].lower():
                city_name = city['name']
                temperature = city['temperature']
                humidity = city['humidity']
                wind_speed = city['wind_speed']

                formatted_data = f"{city_name}, {temperature}, {humidity}, {wind_speed}"
                filtered_data.append(formatted_data)

        result = "\n".join(filtered_data)
        return result

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"



SELECT
    u.username,
    IFNULL(d.expired_domains, 0) AS domains,
    MIN(d.expire_date) AS nearest_expiration
FROM
    users u
LEFT JOIN (
    SELECT
        user_id,
        COUNT(*) AS expired_domains,
        MIN(expiration_date) AS expire_date
    FROM
        domains
    WHERE
        expiration_date > '2022-07-15'
    GROUP BY
        user_id
) d ON u.user_id = d.user_id
WHERE
    u.status = 'active'
GROUP BY
    u.user_id, u.username;






SELECT
    u.username,
    COUNT(d.domain_id) AS domains,
    MIN(d.expire_date) AS nearest_expiration
FROM
    users u
LEFT JOIN (
    SELECT
        user_id,
        domain_id,
        expire_date
    FROM
        domains
    WHERE
        expire_date > '2022-07-15'
) d ON u.user_id = d.user_id
WHERE
    u.status = 'active'
GROUP BY
    u.username
ORDER BY
    u.username ASC;


