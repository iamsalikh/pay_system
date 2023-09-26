from datetime import datetime

from database import get_db
from database.models import Transaction, Card

from transaction import TransactionModel


# Перевод денег с карты на карту
def add_new_transaction_db(data: TransactionModel):
    db = next(get_db())

    # получаем информацию о картах
    card_from = db.query(Card).filter_by(card_number=data.card_from).first()
    card_to = db.query(Card).filter_by(card_number=data.card_to).first()

    # проверка баланса card_from
    if card_from.balance >= data.amount:
        card_from.balance -= data.amount
        card_to.balance += data.balance

        transaction = data.model_dump()
        new_transaction = Transaction(reg_date=datetime.now(), **transaction)

        db.add(new_transaction)
        db.commit()

        return True

    return False


# Вывод всех транзакций по всем картам пользователя
def get_all_payments_db(user_id: int):
    db = next(get_db())

    user_payments = db.query(Transaction).filter_by(user_id=user_id).all()

    return user_payments


# Вывести переводы определенной карты
def get_exact_card_payments_db(user_id: int, card_id: int):
    db = next(get_db())

    all_transactions = db.query(Transaction).filter_by(user_id=user_id, card_from=card_id).all()

    return all_transactions




