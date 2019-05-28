def separate_instruments():
    scores = np.zeros((len(classifiers), Y.shape[1], n_splits))
    skf = StratifiedKFold(n_splits=n_splits, random_state=42)
    for f, (train, test) in enumerate(skf.split(X, encoded_y)):
        X_train, X_test = X[train], X[test]

        for instrument_id, y in enumerate(Y.T):
            print(y, y.shape)
            y_train, y_test = y[train], y[test]

            for clf_id, clf_n in enumerate(classifiers):
                clf = clone(classifiers[clf_n])
                clf.fit(X_train, y_train)
                y_pred = clf.predict(X_test)

                score = balanced_accuracy_score(y_test, y_pred)
                scores[clf_id, instrument_id, f] = score

                print("%i %i %i %.3f" % (f, instrument_id, clf_id, score))
    np.save("separate_instrument", scores)
    return scores