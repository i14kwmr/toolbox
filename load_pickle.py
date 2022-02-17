import argparse
import pickle


def load_pickle(fname):
    with open(fname, "rb") as fid:
        data = pickle.load(fid)

    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fname")
    args = parser.parse_args()

    data = load_pickle(args.fname)
    print(data)
