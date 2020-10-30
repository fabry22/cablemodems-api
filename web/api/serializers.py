from rest_framework import serializers
from api.models import CableModem

class CableModemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CableModem
        fields = ['modem_macaddr', 'ipaddr', 'cmts_ip', 'agentid', 'version', 'mce_concat', 'mce_ver', 'mce_frag', 'mce_phs', 'mce_igmp', 'mce_bpi', 'mce_ds_said', 'mce_us_sid', 'mce_filt_dot1p', 'mce_filt_dot1q', 'mce_tetps', 'mce_ntet', 'mce_dcc', 'thetime', 'offer_time', 'ack_time', 'net_id', 'cluster_id', 'ra_id', 'vsi_devtype', 'vsi_esafetypes', 'vsi_serialno', 'vsi_hwver', 'vsi_swver', 'vsi_bootrom', 'vsi_oui', 'vsi_model', 'vsi_vendor']

class CableModemModelSerializer(serializers.Serializer):
    vendor = serializers.CharField()
    name = serializers.CharField()
    soft = serializers.CharField()

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.vendor = validated_data.get('vendor', instance.vendor)
        instance.name = validated_data.get('name', instance.name)
        instance.soft = validated_data.get('soft', instance.soft)
        instance.save()
        return instance