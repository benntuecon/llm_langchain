from agent.agent import test as agent_test


test_list = []


test_list.append(agent_test)


def main():
    for test in test_list:
        test()


if __name__ == "__main__":
    main()
