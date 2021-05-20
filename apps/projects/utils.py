from django.db.models import Count

from apps.interfaces.models import Interface


def get_count_by_project(datas):
    datas_list = []
    for item in datas:
        project_id = item["id"]
        # 通过id进行分组,计算每个id下的testcases总数量

        get_biubiubiu = Interface.objects.values('id').annotate(testcases=Count('testcases')). \
            filter(project_id=project_id, is_delete=False)
        datas_list.append(get_biubiubiu)
        return datas_list
        # Interface.objects.
#
#
# """
# SELECT `tb_interfaces`.`id`, COUNT(`tb_testcases`.`id`) AS `testcases__count`
# FROM `tb_interfaces` LEFT OUTER JOIN `tb_testcases` ON (`tb_interfaces`.`id` = `tb_testcases`.`interface_id`)
# WHERE (NOT `tb_interfaces`.`is_delete` AND `tb_interfaces`.`project_id` = 1) GROUP BY `tb_interfaces`.`id` ORDER BY NULL
# """


def demo():

    pass

