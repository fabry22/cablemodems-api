from rest_framework import serializers
from api.models import CableModem
from rest_framework.validators import UniqueValidator
from decouple import config

class CableModemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CableModem
        fields = ['modem_macaddr', 'ipaddr', 'cmts_ip', 'agentid', 'version', 'mce_concat', 'mce_ver', 'mce_frag', 'mce_phs', 'mce_igmp', 'mce_bpi', 'mce_ds_said', 'mce_us_sid', 'mce_filt_dot1p', 'mce_filt_dot1q', 'mce_tetps', 'mce_ntet', 'mce_dcc', 'thetime', 'offer_time', 'ack_time', 'net_id', 'cluster_id', 'ra_id', 'vsi_devtype', 'vsi_esafetypes', 'vsi_serialno', 'vsi_hwver', 'vsi_swver', 'vsi_bootrom', 'vsi_oui', 'vsi_model', 'vsi_vendor']

    def create(self, validated_data):
        """
        Create and return a new `CableModem` instance, given the validated data.
        """
        return CableModem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `CableModem` instance, given the validated data.
        """
        instance.modem_macaddr = validated_data.get('modem_macaddr', instance.modem_macaddr)
        instance.ipaddr = validated_data.get('ipaddr', instance.ipaddr)
        instance.cmts_ip = validated_data.get('cmts_ip', instance.cmts_ip)
        instance.agentid = validated_data.get('agentid', instance.agentid)
        instance.version = validated_data.get('version', instance.version)
        instance.mce_concat = validated_data.get('mce_concat', instance.mce_concat)
        instance.mce_ver = validated_data.get('mce_ver', instance.mce_ver)
        instance.mce_frag = validated_data.get('mce_frag', instance.mce_frag)
        instance.mce_phs = validated_data.get('mce_phs', instance.mce_phs)
        instance.mce_igmp = validated_data.get('mce_igmp', instance.mce_igmp)
        instance.mce_bpi = validated_data.get('mce_bpi', instance.mce_bpi)
        instance.mce_ds_said = validated_data.get('mce_ds_said', instance.mce_ds_said)
        instance.mce_us_sid = validated_data.get('mce_us_sid', instance.mce_us_sid)
        instance.mce_filt_dot1p = validated_data.get('mce_filt_dot1p', instance.mce_filt_dot1p)
        instance.mce_filt_dot1q = validated_data.get('mce_filt_dot1q', instance.mce_filt_dot1q)
        instance.mce_tetps = validated_data.get('mce_tetps', instance.mce_tetps)
        instance.mce_ntet = validated_data.get('mce_ntet', instance.mce_ntet)
        instance.mce_dcc = validated_data.get('mce_dcc', instance.mce_dcc)
        instance.thetime = validated_data.get('thetime', instance.thetime)
        instance.offer_time = validated_data.get('offer_time', instance.offer_time)
        instance.ack_time = validated_data.get('ack_time', instance.ack_time)
        instance.net_id = validated_data.get('net_id', instance.net_id)
        instance.cluster_id = validated_data.get('cluster_id', instance.cluster_id)
        instance.ra_id = validated_data.get('ra_id', instance.ra_id)
        instance.vsi_devtype = validated_data.get('vsi_devtype', instance.vsi_devtype)
        instance.vsi_esafetypes = validated_data.get('vsi_esafetypes', instance.vsi_esafetypes)
        instance.vsi_serialno = validated_data.get('vsi_serialno', instance.vsi_serialno)
        instance.vsi_hwver = validated_data.get('vsi_hwver', instance.vsi_hwver)
        instance.vsi_swver = validated_data.get('vsi_swver', instance.vsi_swver)
        instance.vsi_bootrom = validated_data.get('vsi_bootrom', instance.vsi_bootrom)
        instance.vsi_oui = validated_data.get('vsi_oui', instance.vsi_oui)
        instance.vsi_model = validated_data.get('vsi_model', instance.vsi_model)
        instance.vsi_vendor = validated_data.get('vsi_vendor', instance.vsi_vendor)

        instance.save()
        return instance