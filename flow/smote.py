from main import *


def smote():
    scores = np.zeros((len(classifiers), n_splits))
    skf = StratifiedKFold(n_splits=n_splits, random_state=42)
    for f, (train, test) in enumerate(skf.split(X, encoded_y)):
        X_train, X_test = X[train], X[test]
        y_train, y_test = encoded_y[train], encoded_y[test]

        sm = SMOTE(random_state=42)
        X_res, y_res = sm.fit_resample(X_train, y_train)

        for clf_id, clf_n in enumerate(classifiers):
            clf = clone(classifiers[clf_n])
            clf.fit(X_res, y_res)
            y_pred = clf.predict(X_test)

            score = balanced_accuracy_score(y_test, y_pred)
            print(score)

            scores[clf_id, f] = score
    np.save("smote", scores)
    return score


