# Given
def is_number(n):
    try :
        int(n) # activation_fn - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


def cal_precision(tp: int, fp: int):
    """
    Input: True Positive, False Positive
    Output: Precision
    """
    precision = tp / (tp+fp)
    return precision


def cal_recall(tp: int, fn: int):
    """
    Input: True Positive, False Negative
    Output: Recall
    """
    recall = tp / (tp+fn)
    return recall


def cal_f1_score(precision: float, recall: float):
    """
    Input: Precision, Recall
    Output: F1-Score
    """
    f1_score = 2 * (precision*recall) / (precision+recall)
    return f1_score


def check_not_type(var, dtype, name_var):
    """
    Return True if type of var is not suitable
    """
    if isinstance(var, dtype):
        return False
    print(f'{name_var} must be {dtype.__name__}')
    return True


def exercise1(tp: int, fp: int, fn: int):
    """
    Calculate precision, recall, f1-score and print the results
    Input: True Positive, False Positive, False Negative
    Output: None
    """
    if check_not_type(tp, int, 'tp') or check_not_type(fp, int, 'fp') or check_not_type(fn, int, 'fn'):
        return None
    if (tp * fp * fn) <= 0:
        print('tp and fp and fn must be greater than zero')
        return None
    
    precision = cal_precision(tp, fp)
    recall = cal_recall(tp, fn)
    f1_score = cal_f1_score(precision, recall)
    
    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1-score is {f1_score}')


if __name__ == '__main__':
    tp = input('tp = ')
    if not is_number(tp):
        print('tp must be int')
        quit()
    
    fp = input('fp = ')
    if not is_number(fp):
        print('fp must be int')
        quit()

    fn = input('fn = ')
    if not is_number(fn):
        print('fn must be int')
        quit()

    tp = int(tp)
    fp = int(fp)
    fn = int(fn)
    exercise1(tp, fp, fn)