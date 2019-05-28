def full():
    scores = np.zeros((len(classifiers), n_splits))
    skf = StratifiedKFold(n_splits=n_splits, random_state=42)
    for f, (train, test) in enumerate(skf.split(X, encoded_y)):
        X_train, X_test = X[train], X[test]
        y_train, y_test = encoded_y[train], encoded_y[test]

        for clf_id, clf_n in enumerate(classifiers):
            clf = clone(classifiers[clf_n])
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)

            score = balanced_accuracy_score(y_test, y_pred)

            scores[clf_id, f] = score
            print(score)

    np.save("full", scores)
    return scores