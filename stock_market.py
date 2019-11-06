'''
Welcome to Forma.ai stock statement generator! In this problem, you will be coding up a transaction
statement generator for a existing trader on our stock trading system. The inputs are provided below, and
the exact output you are to generate is provided after the inputs.

actions: the timestamped actions that the stock trader performed, it can be BUY or SELL type, and they can
buy or sell a few different stocks. However, you should assume that the number of ticker is not limited to
3 types as in the example below, but potentially infinite, so the ticker should not be hardcoded anywhere.

stock_actions: the timestamped actions that the stock performed regardless of who the trader is. It includes
stock splits, and dividend payouts. Even though these actions are not performed by our trader, it still affects
our trader's portfolios, so it should be recorded in the statement that we prepare.

We are looking for easy to understand/extend program that doesn't perform any unnecessary actions.

Feel free to extend the test cases to include new ones that exercises your program to the fullest.
'''


class Stockpurches:
    """
    The class that represents a Stockpurches. We generate a new Stockpurches every time when we buy a new stock
    each Stockpurches has it's name, price, and number of shares.

    Attributes:
        stock_name (string): The name of the stock we want to add into the budle.
        stock_price (int): The price of the stock when bought it.
        stock_share (int): The number of shares we bought.
    Methods:
        split(int)
        get_price()
        get_share()
        sell_share(int)
    """
    def __init__(self, stock_name, stock_share, stock_price):
        """
        The init funciton for the class trader

        Parameters:
            stock_name (string): The name of the stock we want to add into the budle.

            stock_price (int): The price of the stock when bought it.

            stock_share (int): The number of shares we bought.
        return:
            None
        """
        self.stock_name = stock_name
        self.stock_price = float(stock_price)
        self.stock_share = int(stock_share)

    def __repr__(self):
        return 'Stockpurches(name=' + self.stock_name + ', price=' + str(self.stock_price) +\
               ', share=' + str(self.stock_share) + ')'

    def split(self, split_num):
        """
        the funciton represents the split funciton in stock_actions which divided stock price and mutipile the stock
        share

        Parameters:
            split_num (int): the number of split that is in the stock shares

        return:
            None
        """
        self.stock_price /= float(split_num)
        self.stock_share *= float(split_num)

    def get_price(self):
        """
        it returns the price of this stock when it got purchesed

        Parameters:
            self: the current Stackpurches

        return:
            the price of this stock when it got purchesed
        """
        return self.stock_price

    def get_share(self):
        """
        it returns the shares of this stockpurches that we still have

        Parameters:
            self: the current Stackpurches

        return:
            the shares of this stockpurches that we still have
        """
        return self.stock_share

    def sell_share(self, decrease_by):
        """
        this function that decrease the shares of the current stockpurches by decrease_by. When we sell all our
        stock of this stock purches, we will set decrease_by to self.stock_share.

        Parameters:
            decrease_by: the number you want to decrese the current stockpurches's stockshare by

        return:
            None
        """
        if self.stock_share >= decrease_by:
            self.stock_share -= decrease_by
        else:
            print("Opps, sell_share has an error where you are selling too much in this stockPurches")


class Trader:
    """
    The class that represents a single trader, in our example, there is only one trader
    Attributes:
        stock_bundle (dict): a dictionary that contain the stock name and how many shares the trader has.
        dividend_income (int): The total divided income that come from other companies
    Methods:
        add_dividend_income(float, string):
        add_stock(string, int)
        remove_stock(string,int)
    """
    def __init__(self, stock_bundle, dividend_income):
        """
        The init funciton for the class trader

        Parameters:
            stock_bundle (dict): a dictionary where the key is the stock name, and the vlaue is a list contains
                                class StockInput.

            dividend_income (int): The total divided income that come from other companies

        attribute:
            purches_time(dict): a dictionary that stores the number of times that each stock is purchesed
        """
        self.stock_bundle = stock_bundle
        self.dividend_income = dividend_income

    def __repr__(self):
        return '( Trader(bundle=' + str(self.stock_bundle) + ', dividend_income=' + str(self.dividend_income) + ')'

    def get_total_share(self, stock_name):
        """
        The funciton that returns the number of shares of one stock type

        Parameters:
            stock_name(string): the name of the stock that we want to get the total sale

        Returns:
            (int) the total number of shares of stock_name
        """
        # this is a list contain all the bundle purchease of stock_name
        stock_list = self.stock_bundle[stock_name]
        total_sale = 0
        for stock_purches in stock_list:
            total_sale += int(stock_purches.get_share())
        return total_sale

    def add_dividend_income(self, dividend_rate, stock_name):
        """
        The funciton to add the trader's dividend income by stock_name with the dividend_rate

        Parameters:
            stock_name (string): the name of the stock that want to paid out the dividend money

            dividend_rate(float): the rate of paid out the company provide

        Returns:
            None
        """
        total_sale = self.get_total_share(stock_name)
        self.dividend_income += total_sale * dividend_rate

    def add_stock(self, stock_name, stock_share, stock_price):
        """
        The funciton to add one stock into our stock bundle. if stcok does not exists in our bundle, we create a new key

        Parameters:
            stock_name (string): The name of the stock we want to add into the budle.
            stock_price (int): The price of the stock when bought it.
            stock_share (int): The number of shares we bought.

        Returns:
            None
        """

        new_stock = Stockpurches(stock_name, stock_share, stock_price)
        if stock_name in self.stock_bundle:
            self.stock_bundle[stock_name].append(new_stock)
            self.stock_bundle[stock_name].sort(key=lambda element: element.stock_price)
        else:
            self.stock_bundle[stock_name] = [new_stock]

    def sell_stock(self, stock_name, stock_share_sell, cur_stock_price):
        """
        The funciton sells stocks and with stock_share amount of shares. and calculate profits
        or loss via cureent stock price.

        Parameters:
            stock_name (string): The name of the stock we want to sell from the bundle.
            stock_share_sell (int): The number of shares we want to sell.
            cur_stock_price (int): The current price of the stock.

        Returns:
            a string representation of profit or loss
        """
        cur_stock_price = float(cur_stock_price)
        if stock_name in self.stock_bundle:
            total_share = self.get_total_share(stock_name)
            if total_share >= int(stock_share_sell):
                acc = int(stock_share_sell)
                total_profit = 0
                for single_event_purches in self.stock_bundle[stock_name]:
                    one_purchased_share = single_event_purches.get_share()
                    if one_purchased_share > acc:
                        single_event_purches.sell_share(acc)
                        total_profit += acc * (cur_stock_price - single_event_purches.get_price())
                        break
                    else:
                        acc -= one_purchased_share
                        total_profit += single_event_purches.get_share() * (cur_stock_price - single_event_purches.get_price())
                        single_event_purches.sell_share(one_purchased_share)
                return total_profit
            else:
                print("opps! We do not have enough shares to sell")


class Generator:
    """
    The class that generates the transaction statement from two inputs

    Attributes:
        actions(list): the aciton input from Forma.ai
        stock_actions (list): the stock_action input form Forma.ai

    Methods:
    """
    def __init__(self, actions, stock_actions):
        """
        The init funciton for the class Generator

        Parameters:
            actions (list):  the aciton input from Forma.ai

            stock_actions (list): the stock_action input form Forma.ai
        return:
            None
        """
        self.actions = actions
        self.stock_actions = stock_actions

    def sort_by_time(self, actions, stock_actions):
        """
        return a list of all acitons that is sorted by time

        Parameters:
            actions (list):  the aciton input from Forma.ai

            stock_actions (list): the stock_action input form Forma.ai

        return:
            result(List): the list that contain all action and stock_action sorted by time
        """
        action_size = len(actions)
        stock_actions_size = len(stock_actions)
        res = []
        i, j = 0, 0
        while i < action_size and j < stock_actions_size:
            if actions[i].get('date') < stock_actions[j].get('date'):
                res.append(actions[i])
                i += 1

            else:
                res.append(stock_actions[j])
                j += 1
        res = res + actions[i:] + stock_actions[j:]
        return res

    def create_statement(self, sorted_events, trader):
        """
        return the output statement for trader

        Parameters:
            sorted_events (list): the sorted actions of two inputs

            trader (Trader): the trader we are giving statement to

        return:
            result(str): the final output string
        """
        final_text = ""
        for event in sorted_events:
            if "action" in event:
                final_text += self.create_action_statement(event, trader)
            else:

                final_text += self.create_stock_statement(event, trader)
        return final_text

    def create_action_statement(self, action_event, trader):
        """
        return the output statement for trader of actions input

        Parameters:
            action_event (dict): the sorted actions of action inputs

            trader (Trader): the trader we are giving statement to

        return:
            result(str): the output string of action statement
        """
        action_date = action_event['date'].split(" ")[0]
        action_action = action_event['action']
        action_price = action_event['price']
        action_stock_name = action_event['ticker']
        action_shares = action_event['shares']
        input_action = ""
        action_profit = 0
        if action_action == "BUY":
            trader.add_stock(action_stock_name, action_shares, action_price)
            input_action = "bought"
        elif action_action == "SELL":
            action_profit = trader.sell_stock(action_stock_name, action_shares, action_price)
            input_action = "sold"
        self.get_trader_info_text(trader)
        statement_text = "On {}, you have:\n".format(action_date)
        statement_text += self.get_trader_info_text(trader)
        transaction_text = """Transactions:
        - You {} {} shares of {} at a price of ${} per share""".\
            format(input_action, action_shares, action_stock_name, action_price,)
        if input_action == "sold":
            transaction_text += """ for a profit of ${}""".format(action_profit)
        result_text = statement_text + transaction_text + "\n" + "\n"
        return result_text

    def get_trader_info_text(self, trader):
        """
        return the output statement for trader of his info, such as shares and dividend income

        Parameters:
            trader (Trader): the trader we are giving statement to

        return:
            result(str): the output string of trader's info, such as shares and divided income.
        """
        result_text = ""
        for single_bundle in trader.stock_bundle:
            if trader.get_total_share(single_bundle) != 0:
                bundles = trader.stock_bundle
                income = trader.dividend_income
                shares = 0
                total_num = 0
                for diff_price_bundle in bundles[single_bundle]:
                    if diff_price_bundle.get_price() != 0:
                        shares += diff_price_bundle.get_share()
                        total_num += diff_price_bundle.get_share() * diff_price_bundle.get_price()
                avg_price = total_num/shares
                result_text += """   - {} shares of {} at ${} per share\n """.format(shares, single_bundle,
                                                                                     round(avg_price, 2))
                result_text += """   - ${} of dividend income\n """.format(income)
        return result_text

    def create_stock_statement(self, stock_action_event, trader):
        """
        return the output statement for trader of stock_action input

        Parameters:
            stock_action_event (dict): the sorted actions of stock_action inputs

            trader (Trader): the trader we are giving statement to

        return:
            result(str): the output string of stock_action statement
        """
        action_date = stock_action_event['date']
        action_dividend = stock_action_event['dividend']
        action_split = stock_action_event['split']
        action_stock_name = stock_action_event['stock']
        # for example ABC is not in trader's bundle, so we have to check this case
        if action_stock_name in trader.stock_bundle:
            trader_budnle_name = trader.stock_bundle[action_stock_name]
            if action_split != "":
                for single_purchase in trader_budnle_name:
                    single_purchase.split(action_split)
            if action_dividend != "":
                trader.add_dividend_income(float(action_dividend), action_stock_name)
            result_text = "On {}, you have:\n".format(action_date)
            result_text += self.get_trader_info_text(trader)
            if action_split != "":
                result_text += "- {} split {} to 1, and you have {} shares\n".\
                    format(action_stock_name, action_split, trader.get_total_share(action_stock_name))
            if action_dividend != "":
                result_text += "Transactions:\n - {} paid out ${} dividend per share, and you have {} shares\n".\
                    format(action_stock_name, action_dividend, trader.get_total_share(action_stock_name))
            return result_text + "\n"
        else:
            return ""





# input
actions = [{'date': '1992/07/14 11:12:30', 'action': 'BUY', 'price': '12.3', 'ticker': 'AAPL', 'shares': '500'}, {'date': '1992/09/13 11:15:20', 'action': 'SELL', 'price': '15.3', 'ticker': 'AAPL', 'shares': '100'}, {'date': '1992/10/14 15:14:20', 'action': 'BUY', 'price': '20', 'ticker': 'MSFT', 'shares': '300'}, {'date': '1992/10/17 16:14:30', 'action': 'SELL', 'price': '20.2', 'ticker': 'MSFT', 'shares': '200'}, {'date': '1992/10/19 15:14:20', 'action': 'BUY', 'price': '21', 'ticker': 'MSFT', 'shares': '500'}, {'date': '1992/10/23 16:14:30', 'action': 'SELL', 'price': '18.2', 'ticker': 'MSFT', 'shares': '600'}, {'date': '1992/10/25 10:15:20', 'action': 'SELL', 'price': '20.3', 'ticker': 'AAPL', 'shares': '300'}, {'date': '1992/10/25 16:12:10', 'action': 'BUY', 'price': '18.3', 'ticker': 'MSFT', 'shares': '500'}]

stock_actions = [{'date': '1992/08/14', 'dividend': '0.10', 'split': '', 'stock': 'AAPL'}, {'date': '1992/09/01', 'dividend': '', 'split': '3', 'stock': 'AAPL'}, {'date': '1992/10/15', 'dividend': '0.20', 'split': '', 'stock': 'MSFT'},{'date': '1992/10/16', 'dividend': '0.20', 'split': '', 'stock': 'ABC'}]

# output:

""" 
On 1992-07-14, you have:
    - 500 shares of AAPL at $12.30 per share
    - $0 of dividend income
  Transactions:
    - You bought 500 shares of AAPL at a price of $12.30 per share
On 1992-08-14, you have:
    - 500 shares of AAPL at $12.30 per share
    - $50.00 of dividend income
  Transactions:
    - AAPL paid out $0.10 dividend per share, and you have 500 shares
On 1992-09-01, you have:
    - 1500 shares of AAPL at $4.10 per share
    - $50.00 of dividend income
  Transactions:
    - AAPL split 3 to 1, and you have 1500 shares
On 1992-09-13, you have:
    - 1400 shares of AAPL at $4.10 per share
    - $50.00 of dividend income
  Transactions:
    - You sold 100 shares of AAPL at a price of $15.30 per share for a profit of $1120.00
On 1992-10-14, you have:
    - 1400 shares of AAPL at $4.10 per share
    - 300 shares of MSFT at $20.00 per share
    - $50.00 of dividend income
  Transactions:
    - You bought 300 shares of MSFT at a price of $20.00 per share
On 1992-10-15, you have:
    - 1400 shares of AAPL at $4.10 per share
    - 300 shares of MSFT at $20.00 per share
    - $110.00 of dividend income
  Transactions:
    - MSFT paid out $0.20 dividend per share, and you have 300 shares
On 1992-10-17, you have:
    - 1400 shares of AAPL at $4.10 per share
    - 100 shares of MSFT at $20.00 per share
    - $110.00 of dividend income
  Transactions:
    - You sold 200 shares of MSFT at a price of $20.20 per share for a profit of $40.00
On 1992-10-19, you have:
    - 1400 shares of AAPL at $4.10 per share
    - 600 shares of MSFT at $20.83 per share
    - $110.00 of dividend income
  Transactions:
    - You bought 500 shares of MSFT at a price of $21.00 per share
On 1992-10-23, you have:
    - 1400 shares of AAPL at $4.10 per share
    - $110.00 of dividend income
  Transactions:
    - You sold 600 shares of MSFT at a price of $18.20 per share for a loss of $-1580.00
On 1992-10-25, you have:
    - 1100 shares of AAPL at $4.10 per share
    - 500 shares of MSFT at $18.30 per share
    - $110.00 of dividend income
  Transactions:
    - You sold 300 shares of AAPL at a price of $20.30 per share for a profit of $4860.00
    - You bought 500 shares of MSFT at a price of $18.30 per share
"""

if __name__ == "__main__":
    test_trader = Trader({}, 0)
    stock_generator = Generator(actions, stock_actions)

    sorted_events = stock_generator.sort_by_time(actions, stock_actions)
    Answer = stock_generator.create_statement(sorted_events, test_trader)
    print(Answer)
