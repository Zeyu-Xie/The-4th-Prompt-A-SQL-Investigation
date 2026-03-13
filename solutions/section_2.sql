SELECT
    card_swipes.swipe_id AS swipe_id,
    card_swipes.card_id AS card_id,
    card_swipes.datetime AS datetime,
    id_cards.citizen_id AS citizen_id_on_card,
    id_cards.is_active AS is_active,
    citizens.id AS citizen_id_real
FROM
    card_swipes
    LEFT JOIN id_cards ON card_swipes.card_id = id_cards.card_id
    LEFT JOIN citizens ON citizens.id = id_cards.citizen_id
WHERE
    citizen_id_real IS NULL;