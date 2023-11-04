def get_sql():
    result = ""
    num = 0
    for i in [3001,84,88,1002,200,1003,201,4,101,97,87,41,1,93,40,94,1001,3000,50,1004]:
        num += 1
        this_value = "," + str(i) + "\n,json_value.recall_phase.map_item_count['" + str(
            i) + "'], json_value.recall_phase.map_reference_count['" + str(
            i) + "'], json_value.recall_phase.map_uniq_count['" + str(
            i) + "']\n,json_value.merge_phase.map_item_count['" + str(
            i) + "'], json_value.merge_phase.map_reference_count['" + str(
            i) + "'], json_value.merge_phase.map_uniq_count['" + str(
            i) + "']\n,json_value.pre_rank_phase.map_item_count['" + str(
            i) + "'], json_value.pre_rank_phase.map_reference_count['" + str(
            i) + "'], json_value.pre_rank_phase.map_uniq_count['" + str(
            i) + "']\n,json_value.rank_phase.map_item_count['" + str(
            i) + "'], json_value.pre_rank_phase.map_reference_count['" + str(
            i) + "'], json_value.pre_rank_phase.map_uniq_count['" + str(i) + "']"

        result = result + '\n' + this_value
    print("".join(result))
    print('num is %s'%num)


get_sql()
